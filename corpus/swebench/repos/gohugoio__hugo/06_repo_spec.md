---
name: swebench-gohugoio__hugo
description: SWE-bench repo behavioral spec for gohugoio/hugo. Aggregated from 7 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# gohugoio/hugo — SWE-bench Repo Spec

> **7 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 7 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `hugolib/content_map_page.go` | 3 |
| `tpl/tplimpl/embedded/templates/_default/_markup/render-image.html` | 1 |
| `resources/page/page_paths.go` | 1 |
| `resources/page/pagegroup.go` | 1 |
| `markup/goldmark/blockquotes/blockquotes.go` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: TestPagesSimilarSectionNames, TestEmbeddedImageRenderHookMarkdownAttributes, TestHashSignInPermalink, TestRebuildHomeThenPageIssue12436, TestGetPageContentAdapterBaseIssue12561**

Sample FAIL_TO_PASS test names (first 10):
```
  TestPagesSimilarSectionNames
  TestEmbeddedImageRenderHookMarkdownAttributes
  TestHashSignInPermalink
  TestRebuildHomeThenPageIssue12436
  TestGetPageContentAdapterBaseIssue12561
  TestGroupByParamCalledWithUnavailableParam
  TestBlockquoteHook
```

## Section 4 — Problem-theme distribution

Top themes across 7 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| wrong_output | 3 | 42.9% |
| config_environment | 1 | 14.3% |
| regression | 1 | 14.3% |
| other | 1 | 14.3% |
| documentation | 1 | 14.3% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `gohugoio__hugo-12171`

**Files likely affected**: `hugolib/content_map_page.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestPagesSimilarSectionNames']`

**Problem statement (excerpt):**
> Parent .Pages collection incorrect when adjacent sections are named similarly The issue title isn't great. The problem occurs with v0.123.0 and later.
 
 I ran into this on the Hugo docs site when visiting <https://gohugo.io/methods/>. You should see 10 entries, one for each subsection. Instead, there are 14 entries. The 4 extra entries are regular pages under the "menu" directory. Adjacent to the

### Sample 2 — `gohugoio__hugo-12204`

**Files likely affected**: `tpl/tplimpl/embedded/templates/_default/_markup/render-image.html`
**FAIL_TO_PASS** (1 tests, first 3): `['TestEmbeddedImageRenderHookMarkdownAttributes']`

**Problem statement (excerpt):**
> Embedded image render hook does not honor markdown attributes Reference: <https://discourse.gohugo.io/t/image-block-attribute-disappears-with-0-123-x/48677>
 
 Test case:
 
 '''go
 func TestFoo(t *testing.T) {
 	t.Parallel()
 
 	files := '
 -- config.toml --
 disableKinds = ['page','rss','section','sitemap','taxonomy','term']
 
 [markup.goldmark.parser]
 wrapStandAloneImageWithinParagraph = false

### Sample 3 — `gohugoio__hugo-12343`

**Files likely affected**: `resources/page/page_paths.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestHashSignInPermalink']`

**Problem statement (excerpt):**
> '#' in links causes them to be truncated If the generated link for a resource contains a '#', the link gets truncated.
 
 Given a content file, 'content/posts/hash-in-title.md':
 
 '''yaml
 ---
 title: 'Newsletter #4'
 date: 2024-04-04T12:27:52-07:00
 ---
 Foo
 '''
 
 And a permalinks config in your site config:
 '''yaml
 permalinks:
   posts: "/posts/:year/:month/:slug/"
 '''
 
 You'll wind up wi

### Sample 4 — `gohugoio__hugo-12448`

**Files likely affected**: `hugolib/content_map_page.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestRebuildHomeThenPageIssue12436']`

**Problem statement (excerpt):**
> Page does not reload after modifying a different page Reference: <https://discourse.gohugo.io/t/no-re-rendering-on-document-changes/49465>
 
 '''text
 git clone --single-branch -b hugo-forum-topic-49465 https://github.com/jmooring/hugo-testing hugo-forum-topic-49465
 cd hugo-forum-topic-49465
 hugo server
 '''
 
 Open your browser to 'http://localhost:1313/about/'.
 
 Then in a new console:
 
 '''

### Sample 5 — `gohugoio__hugo-12562`

**Files likely affected**: `hugolib/content_map_page.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestGetPageContentAdapterBaseIssue12561']`

**Problem statement (excerpt):**
> content adapter: Site.GetPage without fully qualified path cannot find page Given that page '/s2/p2' was created by a content adapter:
 
 '''text
 {{ (site.GetPage "/s2/p2").Title }} --> p2  (pass)
 {{ (site.GetPage "p2").Title }}     --> ""  (fail)
 '''
 
 In comparison, when '/s1/p1' is backed by a file:
 
 '''text
 {{ (site.GetPage "/s1/p1").Title }} --> p1  (pass)
 {{ (site.GetPage "p1").Title

### Sample 6 — `gohugoio__hugo-12579`

**Files likely affected**: `resources/page/pagegroup.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestGroupByParamCalledWithUnavailableParam']`

**Problem statement (excerpt):**
> Let PAGES.GroupByParam return nil instead of error Typical construct:
 
 '''text
 {{ range site.Pages.GroupByParam "foo" }}
   <h2>{{ .Key }}</h2>
   {{ range .Pages }}
     <h3><a href="{{ .RelPermalink }}">{{ .LinkTitle }}</a></h3>
   {{ end }}
 {{ end }}
 '''
 
 For an existing site where one or more of the pages contains 'params.foo' in front matter, this works great.
 
 But if none of the pag

### Sample 7 — `gohugoio__hugo-12768`

**Files likely affected**: `markup/goldmark/blockquotes/blockquotes.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestBlockquoteHook']`

**Problem statement (excerpt):**
> Hugo alert heading is case-sensitive and upper case only ([!NOTE]), but GitHub Alert Markdown extension is case-insensitive ([!note]) ### What version of Hugo are you using ('hugo version')?
 
 <pre>
 $ hugo version
 hugo v0.132.1+extended linux/amd64 BuildDate=unknown
 </pre>
 
 ### Does this issue reproduce with the latest release?
 Yes
 
 ---
 
 [Alerts](https://gohugo.io/render-hooks/blockquot

## Section 6 — Builder guidance

When building a fix for an instance in gohugoio/hugo:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. hugolib/content_map_page.go appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 7 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "gohugoio/hugo"`).

First 20 instance_ids:

- `gohugoio__hugo-12171` (dataset: `swe-bench-multilingual-test`)
- `gohugoio__hugo-12204` (dataset: `swe-bench-multilingual-test`)
- `gohugoio__hugo-12343` (dataset: `swe-bench-multilingual-test`)
- `gohugoio__hugo-12448` (dataset: `swe-bench-multilingual-test`)
- `gohugoio__hugo-12562` (dataset: `swe-bench-multilingual-test`)
- `gohugoio__hugo-12579` (dataset: `swe-bench-multilingual-test`)
- `gohugoio__hugo-12768` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
