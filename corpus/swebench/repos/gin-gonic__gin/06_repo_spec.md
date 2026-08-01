---
name: swebench-gin-gonic__gin
description: SWE-bench repo behavioral spec for gin-gonic/gin. Aggregated from 8 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# gin-gonic/gin — SWE-bench Repo Spec

> **8 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 8 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `tree.go` | 2 |
| `routergroup.go` | 1 |
| `binding/binding.go` | 1 |
| `context.go` | 1 |
| `binding/header.go` | 1 |
| `README.md` | 1 |
| `render/reader.go` | 1 |
| `logger.go` | 1 |
| `binding/form_mapping.go` | 1 |
| `gin.go` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: TestMiddlewareCalledOnceByRouterStaticFSNotFound, TestContextBindHeader, TestContextShouldBindHeader, TestContextRenderDataFromReaderNoHeaders, TestReaderRenderNoHeaders**

Sample FAIL_TO_PASS test names (first 10):
```
  TestMiddlewareCalledOnceByRouterStaticFSNotFound
  TestContextBindHeader
  TestContextShouldBindHeader
  TestContextRenderDataFromReaderNoHeaders
  TestReaderRenderNoHeaders
  TestTreeInvalidParamsType
  TestRedirectTrailingSlash
  TestColorForStatus
  TestMappingBaseTypes
  TestMethodNotAllowedNoRoute
```

## Section 4 — Problem-theme distribution

Top themes across 8 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| crash_or_traceback | 3 | 37.5% |
| documentation | 2 | 25.0% |
| other | 1 | 12.5% |
| import_module | 1 | 12.5% |
| config_environment | 1 | 12.5% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `gin-gonic__gin-1805`

**Files likely affected**: `routergroup.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestMiddlewareCalledOnceByRouterStaticFSNotFound']`

**Problem statement (excerpt):**
> Default engine producing two log lines with StaticFS for 404 - go version: 1.11.4
 - gin version (or commit ref): master
 - operating system: OSX, 10.13.6
 
 ## Description
 I am receiving two log lines from a 404, even when using the default engine.
 
 If I remove the router.StaticFS I no longer see the issue.
 
 Code example:
 '''
 func main() {
 	router := gin.Default()
 	router.StaticFS("/", h

### Sample 2 — `gin-gonic__gin-1957`

**Files likely affected**: `binding/binding.go`, `context.go`, `binding/header.go`, `README.md`
**FAIL_TO_PASS** (2 tests, first 3): `['TestContextBindHeader', 'TestContextShouldBindHeader']`

**Problem statement (excerpt):**
> support bind http header param When I refactored some services, I found that gin does not have a function that binds the http header. I think it would be very good if I had this function.
 '''go
 package main
 
 import (
 	"fmt"
 	"github.com/gin-gonic/gin"
 )
 
 type testHeader struct {
 	Rate   int    'header:"Rate"'
 	Domain string 'header:"Domain"'
 }
 
 func main() {
 	r := gin.Default()
 	r.

### Sample 3 — `gin-gonic__gin-2121`

**Files likely affected**: `render/reader.go`
**FAIL_TO_PASS** (2 tests, first 3): `['TestContextRenderDataFromReaderNoHeaders', 'TestReaderRenderNoHeaders']`

**Problem statement (excerpt):**
> DataFromReader with nil extraHeaders crashes ## Description
 
 'gin.Context.DataFromReader' crashes if I don't set extra headers.
 
 I think this little fix would be the best solution to keep API and not to compel me to write 'map[string]string{}' each time.
 
 '''diff
 diff --git a/render/reader.go b/render/reader.go
 index 502d939..fd308a7 100644
 --- a/render/reader.go
 +++ b/render/reader.go
 

### Sample 4 — `gin-gonic__gin-2755`

**Files likely affected**: `tree.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestTreeInvalidParamsType']`

**Problem statement (excerpt):**
> Using gin.CreateTestContext, and then engine.HandleContext causes panic if params are not filled in ## Description
 
 Panic in tree.go:446 when calling router.HandleContext on a context that does not have params parsed
 
 ## How to reproduce
 
 '''
 package main
 
 import (
 	"fmt"
 	"net/http"
 	"net/http/httptest"
 
 	"github.com/gin-gonic/gin"
 )
 
 func main() {
 	w := httptest.NewRecorder()
 

### Sample 5 — `gin-gonic__gin-3227`

**Files likely affected**: `tree.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestRedirectTrailingSlash']`

**Problem statement (excerpt):**
> RedirectFixedPath redirecting trailing slashes ## Description
 
 RedirectFixedPath is redirecting trailing slashes regardless of the RedirectTrailingSlash setting.
 
 In [gin.go](https://github.com/gin-gonic/gin/blob/master/gin.go#L73) there is a comment that the RedirectTrailingSlash is independent, but then the comment does not indicate that the behavior would be to also redirect trailing slashe

### Sample 6 — `gin-gonic__gin-3741`

**Files likely affected**: `logger.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestColorForStatus']`

**Problem statement (excerpt):**
> Logging colour for < 200 should be white? ## Description
 
 When the logger logs a response with a status code < 200 it is coloured red:
 
 https://github.com/gin-gonic/gin/blob/c2ba8f19ec19914b73290c53a32de479cd463555/logger.go#L81-L95
 
 Http status codes under 200 are informative rather than errors. Would it be better for < 200 to be white?
 
 I notice this with web socket switching: https://de

### Sample 7 — `gin-gonic__gin-3820`

**Files likely affected**: `binding/form_mapping.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestMappingBaseTypes']`

**Problem statement (excerpt):**
> Binding a non mandatory file parameter will directly result in an error message - With issues:
   - Use the search tool before opening a new issue.
   - Please provide source code and commit sha if you found a bug.
   - Review existing issues and provide feedback or react to them.
 
 ## Description
 
 Bind a a non mandatory file parameter will report an error. 
 
 ## How to reproduce
  
 '''
 
 pa

### Sample 8 — `gin-gonic__gin-4003`

**Files likely affected**: `gin.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestMethodNotAllowedNoRoute']`

**Problem statement (excerpt):**
> runtime error: makeslice: cap out of range when HandleMethodNotAllowed=true and no request handler registered ## Description
 Gin server panics with 'runtime error: makeslice: cap out of range' when 'HandleMethodNotAllowed' is set to 'true' and no handler are registered.
 
 ## How to reproduce
 '''go
 package main
 
 import (
 	"net/http/httptest"
 
 	"github.com/gin-gonic/gin"
 )
 
 func main() {

## Section 6 — Builder guidance

When building a fix for an instance in gin-gonic/gin:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. tree.go appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 8 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "gin-gonic/gin"`).

First 20 instance_ids:

- `gin-gonic__gin-1805` (dataset: `swe-bench-multilingual-test`)
- `gin-gonic__gin-1957` (dataset: `swe-bench-multilingual-test`)
- `gin-gonic__gin-2121` (dataset: `swe-bench-multilingual-test`)
- `gin-gonic__gin-2755` (dataset: `swe-bench-multilingual-test`)
- `gin-gonic__gin-3227` (dataset: `swe-bench-multilingual-test`)
- `gin-gonic__gin-3741` (dataset: `swe-bench-multilingual-test`)
- `gin-gonic__gin-3820` (dataset: `swe-bench-multilingual-test`)
- `gin-gonic__gin-4003` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
