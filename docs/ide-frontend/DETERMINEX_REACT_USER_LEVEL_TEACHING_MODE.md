# React User Level / Teaching Mode

> Locked under
> `locks/sentinel/DETERMINEX_REACT_USER_LEVEL_TEACHING_MODE_LOCK_001.json`.

Rung 8. User-level / teaching-window controls at
`frontend/src/components/ide-product-shell/UserLevelTeachingMode.tsx`.

## 8 levels

`beginner_no_experience`, `learner`, `vibe_coder`,
`junior_developer`, `professional_developer`, `maintainer`,
`security_conscious_operator`, `power_user`.

## Hard rules

The four invariants are **compile-time constants**, not derived
from the chosen level:

```ts
const proofStatusVisible = true;
const authorityGatesActive = true;
const teachingWindowExplainsBlockedReason = true;
const trainingStaysFalse = true;
```

Tests forbid any code pattern that ties authority to level:
`if (level === ...)`, `loosenGates`, `disableGate`, `bypassProof`.

## Captions

- "Beginner mode does NOT hide proof."
- "Professional / power mode does NOT bypass proof."
- "User level changes EXPLANATION DETAIL only — never authority."
