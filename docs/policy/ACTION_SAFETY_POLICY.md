# Action Safety Policy

**Date:** 2026-05-27  
**Status:** Implemented and active  
**Implementation:** `scripts/agents/safety_governor.py`

---

## Overview

The Action Safety Governor (L5) runs before every action the visual/browser/desktop/mobile agent executes. It is the second of two safety layers: L0-L4 filter what gets built; L5 filters what the agent *does* with the world.

L5 is fail-closed. An evaluation error denies the action.

---

## Decision Values

| Decision | Meaning |
|---|---|
| `ALLOW` | Action may proceed without notification |
| `ALLOW_WITH_AUDIT` | Action proceeds but is logged to `audit/` corpus |
| `REQUIRE_CONFIRMATION` | Human confirmation required before execution |
| `BLOCK` | Action is categorically denied and logged to `safety_refusal` corpus |
| `SANDBOX_ONLY` | Action allowed only inside VM/emulator/isolated browser profile |

---

## Mandatory Confirmation Actions

These actions require explicit human confirmation regardless of task context:

| Action | Reason |
|---|---|
| `SEND_MESSAGE` | Irreversible external communication |
| `SUBMIT_FORM` | May trigger purchases, subscriptions, legal agreements |
| `MAKE_PURCHASE` | Irreversible financial transaction |
| `DELETE_DATA` | Destructive, often irreversible |
| `UPLOAD_FILE` | Data leaves local scope |
| `DOWNLOAD_FILE` | External content enters scope |
| `ENTER_CREDENTIAL` | Credential exposure risk |
| `INSTALL_SOFTWARE` | Modifies system state |
| `GRANT_PERMISSION` | Expands attack surface |
| `ACCESS_CONTACTS` | Privacy-sensitive |
| `ACCESS_LOCATION` | Privacy-sensitive |
| `ACCESS_CAMERA` | Covert surveillance risk |
| `ACCESS_MIC` | Covert surveillance risk |
| `CHANGE_SECURITY_SETTING` | Changes system trust boundary |
| `DEPLOY_OR_PUBLISH` | Irreversible, external-facing |

---

## Absolute Block Patterns

These action intents are blocked regardless of task spec or user instruction:

- Credential theft (collecting credentials without disclosure)
- Covert surveillance (monitoring without consent)
- Doxxing (aggregating identity data for targeting)
- Harassment automation (bulk messaging, contact bombing)
- Spam automation (bulk unsolicited email/SMS)
- Dark pattern deployment (fake urgency, misdirection, hidden unsubscribe)
- Non-consensual tracking (location/behavior without disclosure)
- Malware persistence (registry/startup/cron without consent)
- Reverse shell setup
- Unauthorized data exfiltration

---

## Sandbox Requirements

| Environment | Requirement | Block if Absent |
|---|---|---|
| Desktop | VM (VirtualBox/QEMU/Hyper-V) | Yes |
| Mobile | Android emulator (not physical device) | Yes |
| Browser | Isolated Playwright profile | Yes |
| Cloud vision API | Visual Cloak PII redaction active | Yes |

---

## Risk Levels

| Risk | Actions | Default Decision |
|---|---|---|
| `MINIMAL` | READ_SCREEN, READ_DOM, READ_ACCESSIBILITY_TREE, SCROLL | ALLOW |
| `LOW` | CLICK, PRESS_KEY, TYPE (non-credential fields) | ALLOW_WITH_AUDIT |
| `MEDIUM` | OPEN_APP, SWITCH_WINDOW, RUN_COMMAND (read-only) | ALLOW_WITH_AUDIT |
| `HIGH` | EDIT_FILE, APPLY_PATCH, UPLOAD_FILE, DOWNLOAD_FILE | REQUIRE_CONFIRMATION |
| `CRITICAL` | SUBMIT_FORM, SEND_MESSAGE, MAKE_PURCHASE, DELETE_DATA, DEPLOY_OR_PUBLISH | REQUIRE_CONFIRMATION |
| `ABSOLUTE` | Any action matching block pattern list | BLOCK |

---

## Integration Points

Every controller must call `safety_governor.evaluate_action(task, observation, action)` before executing:

```python
# Pattern used by every controller
decision = governor.evaluate_action(task, observation, action)
if decision.value == "BLOCK":
    corpus_manager.write_refusal(task, action, decision)
    raise ActionBlocked(decision.reason)
elif decision.value == "REQUIRE_CONFIRMATION":
    if not get_human_confirmation(action):
        corpus_manager.write_refusal(task, action, decision)
        raise ActionBlocked("User declined confirmation")
```

---

## Refusal Corpus

Every blocked action and declined confirmation is written to `T:/determinex_corpus/safety_refusal/YYYY-MM-DD.jsonl`. These are training signal for the Sentinel — the system learns what *not* to do from real refusals.

---

*Determinex Action Safety Policy · Ryan Gurganious · 2026-05-27*
