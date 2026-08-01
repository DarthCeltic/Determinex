---
name: swebench-psf__requests
description: SWE-bench repo behavioral spec for psf/requests. Aggregated from 58 bug-fix instances across 3 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# psf/requests — SWE-bench Repo Spec

> **58 bug-fix instances** across 3 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-test | 44 |
| swe-bench-verified-test | 8 |
| swe-bench-lite-test | 6 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `requests/models.py` | 23 |
| `requests/sessions.py` | 21 |
| `requests/utils.py` | 10 |
| `requests/adapters.py` | 6 |
| `requests/auth.py` | 4 |
| `requests/cookies.py` | 2 |
| `requests/compat.py` | 2 |
| `requests/packages/__init__.py` | 2 |
| `requests/structures.py` | 1 |
| `requests/packages/urllib3/response.py` | 1 |
| `requests/packages/urllib3/connectionpool.py` | 1 |
| `requests/packages/urllib3/util/retry.py` | 1 |
| `requests/packages/urllib3/__init__.py` | 1 |
| `requests/packages/urllib3/contrib/appengine.py` | 1 |
| `requests/packages/urllib3/poolmanager.py` | 1 |
| `requests/packages/urllib3/util/connection.py` | 1 |
| `requests/packages/urllib3/util/response.py` | 1 |
| `requests/packages/urllib3/request.py` | 1 |
| `requests/packages/urllib3/connection.py` | 1 |
| `requests/packages/urllib3/contrib/pyopenssl.py` | 1 |
| `requests/packages/urllib3/exceptions.py` | 1 |
| `requests/packages/urllib3/util/ssl_.py` | 1 |
| `requests/packages.py` | 1 |
| `requests/exceptions.py` | 1 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  test_requests.py::RequestsTestCase::test_DIGESTAUTH_QUOTES_QOP_VALUE
  test_requests.py::RequestsTestCase::test_DIGESTAUTH_WRONG_HTTP_401_GET
  test_requests.py::RequestsTestCase::test_DIGEST_AUTH_RETURNS_COOKIE
  test_requests.py::RequestsTestCase::test_DIGEST_HTTP_200_OK_GET
  test_requests.py::RequestsTestCase::test_POSTBIN_GET_POST_FILES_WITH_DATA
  test_requests.py::RequestsTestCase::test_DIGEST_AUTH_RETURNS_COOKIE
  test_requests.py::RequestsTestCase::test_HTTP_200_OK_GET_ALTERNATIVE
  test_requests.py::RequestsTestCase::test_HTTP_200_OK_HEAD
  test_requests.py::RequestsTestCase::test_POSTBIN_GET_POST_FILES
  test_requests.py::RequestsTestCase::test_auth_is_stripped_on_redirect_off_host
```

## Section 4 — Problem-theme distribution

Top themes across 58 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| crash_or_traceback | 16 | 27.6% |
| wrong_output | 10 | 17.2% |
| regression | 9 | 15.5% |
| other | 9 | 15.5% |
| encoding_unicode | 5 | 8.6% |
| documentation | 4 | 6.9% |
| import_module | 3 | 5.2% |
| config_environment | 1 | 1.7% |
| type_handling | 1 | 1.7% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `psf__requests-1963`

**Files likely affected**: `requests/sessions.py`
**FAIL_TO_PASS** (7 tests, first 3): `['test_requests.py::RequestsTestCase::test_DIGESTAUTH_QUOTES_QOP_VALUE', 'test_requests.py::RequestsTestCase::test_DIGESTAUTH_WRONG_HTTP_401_GET', 'test_requests.py::RequestsTestCase::test_DIGEST_AUTH_RETURNS_COOKIE']`

**Problem statement (excerpt):**
> 'Session.resolve_redirects' copies the original request for all subsequent requests, can cause incorrect method selection Consider the following redirection chain:  ''' POST /do_something HTTP/1.1 Host: server.example.com ...  HTTP/1.1 303 See Other Location: /new_thing_1513  GET /new_thing_1513 Host: server.example.com ...  HTTP/1.1 307 Temporary Redirect Location: //failover.example.com/new_thin

### Sample 2 — `psf__requests-2148`

**Files likely affected**: `requests/models.py`
**FAIL_TO_PASS** (10 tests, first 3): `['test_requests.py::RequestsTestCase::test_DIGEST_AUTH_RETURNS_COOKIE', 'test_requests.py::RequestsTestCase::test_HTTP_200_OK_GET_ALTERNATIVE', 'test_requests.py::RequestsTestCase::test_HTTP_200_OK_HEAD']`

**Problem statement (excerpt):**
> socket.error exception not caught/wrapped in a requests exception (ConnectionError perhaps?) I just noticed a case where I had a socket reset on me, and was raised to me as a raw socket error as opposed to something like a requests.exceptions.ConnectionError:  '''   File "/home/rtdean/***/***/***/***/***/***.py", line 67, in dir_parse     root = ElementTree.fromstring(response.text)   File "/home/

### Sample 3 — `psf__requests-2317`

**Files likely affected**: `requests/sessions.py`
**FAIL_TO_PASS** (8 tests, first 3): `['test_requests.py::RequestsTestCase::test_HTTP_302_ALLOW_REDIRECT_GET', 'test_requests.py::RequestsTestCase::test_POSTBIN_GET_POST_FILES', 'test_requests.py::RequestsTestCase::test_POSTBIN_GET_POST_FILES_WITH_DATA']`

**Problem statement (excerpt):**
> method = builtin_str(method) problem In requests/sessions.py is a command:  method = builtin_str(method) Converts method from b'GET' to "b'GET'"  Which is the literal string, no longer a binary string.  When requests tries to use the method "b'GET'", it gets a 404 Not Found response.  I am using python3.4 and python-neutronclient (2.3.9) with requests (2.4.3).  neutronclient is broken because it u

### Sample 4 — `psf__requests-2674`

**Files likely affected**: `requests/adapters.py`
**FAIL_TO_PASS** (12 tests, first 3): `['test_requests.py::RequestsTestCase::test_BASICAUTH_TUPLE_HTTP_200_OK_GET', 'test_requests.py::RequestsTestCase::test_HTTP_200_OK_GET_ALTERNATIVE', 'test_requests.py::RequestsTestCase::test_HTTP_200_OK_GET_WITH_PARAMS']`

**Problem statement (excerpt):**
> urllib3 exceptions passing through requests API I don't know if it's a design goal of requests to hide urllib3's exceptions and wrap them around requests.exceptions types.  (If it's not IMHO it should be, but that's another discussion)  If it is, I have at least two of them passing through that I have to catch in addition to requests' exceptions. They are requests.packages.urllib3.exceptions.Decod

### Sample 5 — `psf__requests-3362`

**Files likely affected**: `requests/utils.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_requests.py::TestRequests::test_response_decode_unicode']`

**Problem statement (excerpt):**
> Uncertain about content/text vs iter_content(decode_unicode=True/False) When requesting an application/json document, I'm seeing 'next(r.iter_content(16*1024, decode_unicode=True))' returning bytes, whereas 'r.text' returns unicode. My understanding was that both should return a unicode object. In essence, I thought "iter_content" was equivalent to "iter_text" when decode_unicode was True. Have I 

### Sample 6 — `psf__requests-863`

**Files likely affected**: `requests/models.py`
**FAIL_TO_PASS** (4 tests, first 3): `['tests/test_requests.py::RequestsTestSuite::test_POSTBIN_GET_POST_FILES_WITH_HEADERS', 'tests/test_requests.py::RequestsTestSuite::test_nonurlencoded_postdata', 'tests/test_requests.py::RequestsTestSuite::test_prefetch_redirect_bug']`

**Problem statement (excerpt):**
> Allow lists in the dict values of the hooks argument Currently the Request class has a .register_hook() method but it parses the dictionary it expects from it's hooks argument weirdly: the argument can only specify one hook function per hook.  If you pass in a list of hook functions per hook the code in Request.**init**() will wrap the list in a list which then fails when the hooks are consumed (s

### Sample 7 — `psf__requests-1142`

**Files likely affected**: `requests/models.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test_requests.py::RequestsTestCase::test_no_content_length']`

**Problem statement (excerpt):**
> requests.get is ALWAYS sending content length Hi,  It seems like that request.get always adds 'content-length' header to the request. I think that the right behavior is not to add this header automatically in GET requests or add the possibility to not send it.  For example http://amazon.com returns 503 for every get request that contains 'content-length' header.  Thanks,  Oren  

### Sample 8 — `psf__requests-1724`

**Files likely affected**: `requests/sessions.py`
**FAIL_TO_PASS** (6 tests, first 3): `['test_requests.py::RequestsTestCase::test_DIGEST_AUTH_RETURNS_COOKIE', 'test_requests.py::RequestsTestCase::test_DIGEST_HTTP_200_OK_GET', 'test_requests.py::RequestsTestCase::test_different_encodings_dont_break_post']`

**Problem statement (excerpt):**
> Unicode method names cause UnicodeDecodeError for some requests in Python 2.7.2 The following example works fine:  ''' files = {u'file': open(u'/usr/bin/diff', u'rb')} response = requests.request(method='POST', url=u'http://httpbin.org/post', files=files) '''  But the following example (using 'method=u'POST'' instead of 'method='POST'') produces a UnicodeDecodeError:  ''' files = {u'file': open(u'

## Section 6 — Builder guidance

When building a fix for an instance in psf/requests:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. requests/models.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 58 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "psf/requests"`).

First 20 instance_ids:

- `psf__requests-1963` (dataset: `swe-bench-lite-test`)
- `psf__requests-2148` (dataset: `swe-bench-lite-test`)
- `psf__requests-2317` (dataset: `swe-bench-lite-test`)
- `psf__requests-2674` (dataset: `swe-bench-lite-test`)
- `psf__requests-3362` (dataset: `swe-bench-lite-test`)
- `psf__requests-863` (dataset: `swe-bench-lite-test`)
- `psf__requests-1142` (dataset: `swe-bench-verified-test`)
- `psf__requests-1724` (dataset: `swe-bench-verified-test`)
- `psf__requests-1766` (dataset: `swe-bench-verified-test`)
- `psf__requests-1921` (dataset: `swe-bench-verified-test`)
- `psf__requests-2317` (dataset: `swe-bench-verified-test`)
- `psf__requests-2931` (dataset: `swe-bench-verified-test`)
- `psf__requests-5414` (dataset: `swe-bench-verified-test`)
- `psf__requests-6028` (dataset: `swe-bench-verified-test`)
- `psf__requests-1142` (dataset: `swe-bench-full-test`)
- `psf__requests-1327` (dataset: `swe-bench-full-test`)
- `psf__requests-1339` (dataset: `swe-bench-full-test`)
- `psf__requests-1376` (dataset: `swe-bench-full-test`)
- `psf__requests-1537` (dataset: `swe-bench-full-test`)
- `psf__requests-1635` (dataset: `swe-bench-full-test`)
- ... (38 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
