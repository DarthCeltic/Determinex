---
name: swebench-axios__axios
description: SWE-bench repo behavioral spec for axios/axios. Aggregated from 10 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# axios/axios — SWE-bench Repo Spec

> **10 bug-fix instances** across 2 dataset(s); language(s): js, python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 6 |
| multi-swe-bench | 4 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `lib/adapters/http.js` | 4 |
| `index.d.ts` | 3 |
| `lib/utils.js` | 3 |
| `lib/core/AxiosHeaders.js` | 2 |
| `lib/helpers/toFormData.js` | 2 |
| `package.json` | 2 |
| `lib/defaults/index.js` | 2 |
| `lib/helpers/formDataToStream.js` | 1 |
| `.eslintrc.cjs` | 1 |
| `lib/helpers/readBlob.js` | 1 |
| `lib/env/classes/FormData.js` | 1 |
| `lib/helpers/isAbsoluteURL.js` | 1 |
| `lib/adapters/adapters.js` | 1 |
| `lib/helpers/buildURL.js` | 1 |
| `lib/helpers/Serializers.js` | 1 |
| `lib/core/Axios.js` | 1 |
| `lib/helpers/AxiosURLSearchParams.js` | 1 |
| `index.d.cts` | 1 |
| `lib/helpers/toURLEncodedForm.js` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: supports http with nodejs should properly support default max body length (follow-redirects as well), supports http with nodejs should respect the timeoutErrorMessage property, issues 5028 should handle set-cookie headers as an array, supports http with nodejs FormData SpecCompliant FormData should allow passing FormData, supports http with nodejs compression algorithms GZIP decompression should support decompression**

Sample FAIL_TO_PASS test names (first 10):
```
  supports http with nodejs should properly support default max body length (follow-redirects as well)
  supports http with nodejs should respect the timeoutErrorMessage property
  issues 5028 should handle set-cookie headers as an array
  supports http with nodejs FormData SpecCompliant FormData should allow passing FormData
  supports http with nodejs compression algorithms GZIP decompression should support decompression
  supports http with nodejs compression algorithms GZIP decompression should not fail if response content-length header is missing (GZIP)
  supports http with nodejs compression algorithms GZIP decompression should not fail with chunked responses (without Content-Length header)
  Server-Side Request Forgery (SSRF) should not fetch bad server
```

## Section 4 — Problem-theme distribution

Top themes across 10 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| wrong_output | 3 | 50.0% |
| other | 2 | 33.3% |
| performance | 1 | 16.7% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `axios__axios-4731`

**Files likely affected**: `lib/adapters/http.js`
**FAIL_TO_PASS** (1 tests, first 3): `['supports http with nodejs should properly support default max body length (follow-redirects as well)']`

**Problem statement (excerpt):**
> Unexpected default 'maxBodyLength' enforcement by 'follow-redirects' #### Describe the bug
 As part of the upgrade of 'follow-redirects' in https://github.com/axios/axios/pull/2689, a default 'maxBodyLength' of 10MB began to be enforced (previously, there was no request payload limit). There are a few issues with this:
 1. The default limit is not mentioned in the 'axios' documentation
 2. This ch

### Sample 2 — `axios__axios-4738`

**Files likely affected**: `lib/adapters/http.js`
**FAIL_TO_PASS** (1 tests, first 3): `['supports http with nodejs should respect the timeoutErrorMessage property']`

**Problem statement (excerpt):**
> The timeoutErrorMessage property in config not work with Node.js <!-- Click "Preview" for a more readable version --
 
 Please read and follow the instructions before submitting an issue:
 
 - Read all our documentation, especially the [README](https://github.com/axios/axios/blob/master/README.md). It may contain information that helps you solve your issue.
 - Ensure your issue isn't already [repo

### Sample 3 — `axios__axios-5085`

**Files likely affected**: `index.d.ts`, `lib/core/AxiosHeaders.js`
**FAIL_TO_PASS** (1 tests, first 3): `['issues 5028 should handle set-cookie headers as an array']`

**Problem statement (excerpt):**
> AxiosHeaders get 'set-cookie' returns string instead of array #### Describe the bug
 With version 0.27.2 or older when reading the 'response.headers['set-cookie']' it returned an array of cookies.
 '''
 'set-cookie': [
     'something=else; path=/; expires=Wed, 12 Apr 2023 12:05:15 GMT; samesite=lax; secure; httponly',
     'something-ssr.sig=n4MlwVAaxQAxhbdJO5XbUpDw-lA; path=/; expires=Wed, 12 Ap

### Sample 4 — `axios__axios-5316`

**Files likely affected**: `lib/helpers/toFormData.js`, `lib/helpers/formDataToStream.js`, `lib/utils.js`, `lib/adapters/http.js`, `.eslintrc.cjs`
**FAIL_TO_PASS** (1 tests, first 3): `['supports http with nodejs FormData SpecCompliant FormData should allow passing FormData']`

**Problem statement (excerpt):**
> Using FormData type from Node.js 18 global leads to an error. ### Describe the bug  When the request data value is an instance of the Node.js 18 FormData class the Axios throws the error with the next message. 
 '''Data after transformation must be a string, an ArrayBuffer, a Buffer, or a Stream'''
 Seems like the error goes from this part of the code:
 https://github.com/axios/axios/blob/d032edda

### Sample 5 — `axios__axios-5892`

**Files likely affected**: `lib/adapters/http.js`
**FAIL_TO_PASS** (3 tests, first 3): `['supports http with nodejs compression algorithms GZIP decompression should support decompression', 'supports http with nodejs compression algorithms GZIP decompression should not fail if response content-length header is missing (GZIP)', 'supports http with nodejs compression algorithms GZIP decompression should not fail with chunked responses (without Content-Length header)']`

**Problem statement (excerpt):**
> Header content-encoding isn't automatically convert to lower case. ### Describe the bug  Many services respond with header['content-encoding'] in many forms: 'Gzip', 'GZIP', 'GZip'. My example is connected with downloading from storage.googleapis.com. Response header content-encoding has value 'GZIP' and it is a reason why axios don't decompress content. In my opinion header value should be case-i

### Sample 6 — `axios__axios-6539`

**Files likely affected**: `lib/helpers/isAbsoluteURL.js`
**FAIL_TO_PASS** (1 tests, first 3): `['Server-Side Request Forgery (SSRF) should not fetch bad server']`

**Problem statement (excerpt):**
> Server-Side Request Forgery Vulnerability (CVE-2024-39338) ### Describe the bug  Axios is vulnerable to a Server-Side Request Forgery attack caused by unexpected behaviour where requests for path relative URLS gets processed as protocol relative URLs.
 
 This could be leveraged by an attacker to perform arbitrary requests from the server, potentially accessing internal systems or exfiltrating sens

## Section 6 — Builder guidance

When building a fix for an instance in axios/axios:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. lib/adapters/http.js appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 10 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "axios/axios"`).

First 20 instance_ids:

- `axios__axios-4731` (dataset: `swe-bench-multilingual-test`)
- `axios__axios-4738` (dataset: `swe-bench-multilingual-test`)
- `axios__axios-5085` (dataset: `swe-bench-multilingual-test`)
- `axios__axios-5316` (dataset: `swe-bench-multilingual-test`)
- `axios__axios-5892` (dataset: `swe-bench-multilingual-test`)
- `axios__axios-6539` (dataset: `swe-bench-multilingual-test`)
- `axios__axios-5919` (dataset: `multi-swe-bench`)
- `axios__axios-5661` (dataset: `multi-swe-bench`)
- `axios__axios-5338` (dataset: `multi-swe-bench`)
- `axios__axios-5085` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
