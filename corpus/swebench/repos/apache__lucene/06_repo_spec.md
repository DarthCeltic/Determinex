---
name: swebench-apache__lucene
description: SWE-bench repo behavioral spec for apache/lucene. Aggregated from 9 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# apache/lucene — SWE-bench Repo Spec

> **9 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 9 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `lucene/CHANGES.txt` | 5 |
| `lucene/queries/src/java/org/apache/lucene/queries/intervals/IntervalBuilder.java` | 1 |
| `lucene/core/src/java/org/apache/lucene/document/ShapeField.java` | 1 |
| `lucene/queryparser/src/java/org/apache/lucene/queryparser/classic/MultiFieldQueryParser.java` | 1 |
| `lucene/facet/src/java/org/apache/lucene/facet/DrillSidewaysScorer.java` | 1 |
| `lucene/core/src/java/org/apache/lucene/index/SegmentInfos.java` | 1 |
| `lucene/analysis/opennlp/src/java/org/apache/lucene/analysis/opennlp/OpenNLPSentenceBreakIterator.java` | 1 |
| `lucene/core/src/java/org/apache/lucene/geo/XYCircle.java` | 1 |
| `lucene/core/src/java/org/apache/lucene/geo/Circle.java` | 1 |
| `lucene/core/src/java/org/apache/lucene/geo/XYPoint.java` | 1 |
| `lucene/core/src/java/org/apache/lucene/geo/Point.java` | 1 |
| `lucene/core/src/java/org/apache/lucene/geo/Rectangle2D.java` | 1 |
| `lucene/facet/src/java/org/apache/lucene/facet/StringValueFacetCounts.java` | 1 |
| `lucene/core/src/java/org/apache/lucene/geo/GeoEncodingUtils.java` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: org.apache.lucene.queries.intervals.TestIntervalBuilder > testEmptyIntervals, org.apache.lucene.document.TestLatLonShape > testFlatPolygonDoesNotContainIntersectingLine, org.apache.lucene.queryparser.classic.TestMultiFieldQueryParser > testBoostsSimple, org.apache.lucene.facet.TestDrillSideways > testDrillSidewaysSearchUseCorrectIterator, org.apache.lucene.index.TestIndexWriter > testGetCommitDataFromOldSnapshot**

Sample FAIL_TO_PASS test names (first 10):
```
  org.apache.lucene.queries.intervals.TestIntervalBuilder > testEmptyIntervals
  org.apache.lucene.document.TestLatLonShape > testFlatPolygonDoesNotContainIntersectingLine
  org.apache.lucene.queryparser.classic.TestMultiFieldQueryParser > testBoostsSimple
  org.apache.lucene.facet.TestDrillSideways > testDrillSidewaysSearchUseCorrectIterator
  org.apache.lucene.index.TestIndexWriter > testGetCommitDataFromOldSnapshot
  org.apache.lucene.analysis.opennlp.TestOpenNLPSentenceBreakIterator > testPrecedingWithTwoSentences
  org.apache.lucene.geo.TestXYPoint > testEqualsAndHashCode
  TestStringValueFacetCounts > testEmptyMatchset
  TestLatLonDocValuesQueries > testNarrowPolygonCloseToNorthPole
```

## Section 4 — Problem-theme distribution

Top themes across 9 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| crash_or_traceback | 4 | 44.4% |
| wrong_output | 2 | 22.2% |
| other | 2 | 22.2% |
| documentation | 1 | 11.1% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `apache__lucene-11760`

**Files likely affected**: `lucene/queries/src/java/org/apache/lucene/queries/intervals/IntervalBuilder.java`
**FAIL_TO_PASS** (1 tests, first 3): `['org.apache.lucene.queries.intervals.TestIntervalBuilder > testEmptyIntervals']`

**Problem statement (excerpt):**
> IntervalBuilder.NO_INTERVALS returns wrong docId when unpositioned ### Description  DocIdSetIterators should return -1 when they are unpositioned, but 
 IntervalBuilder.NO_INTERVALS always returns NO_MORE_DOCS.  This
 can lead to exceptions when an empty interval query (for example, a
 text string made entirely of stopwords) is combined in a conjunction.  ### Version and environment details  _No r

### Sample 2 — `apache__lucene-12022`

**Files likely affected**: `lucene/CHANGES.txt`, `lucene/core/src/java/org/apache/lucene/document/ShapeField.java`
**FAIL_TO_PASS** (1 tests, first 3): `['org.apache.lucene.document.TestLatLonShape > testFlatPolygonDoesNotContainIntersectingLine']`

**Problem statement (excerpt):**
> Very flat polygons give incorrect 'contains' result ### Description  When performing a search using a shape geometry query of relation type 'QueryRelation.CONTAINS', it is possible to get a false positive when two geometries intersect, but neither actually contains the other. This happens if the indexed geometry is a polygon that is so flat that one of its triangles is simplified to a single line 

### Sample 3 — `apache__lucene-12196`

**Files likely affected**: `lucene/CHANGES.txt`, `lucene/queryparser/src/java/org/apache/lucene/queryparser/classic/MultiFieldQueryParser.java`
**FAIL_TO_PASS** (1 tests, first 3): `['org.apache.lucene.queryparser.classic.TestMultiFieldQueryParser > testBoostsSimple']`

**Problem statement (excerpt):**
> Slop is missing when boost is passed to MultiFieldQueryParser (Since Lucene 5.4.0) ### Description  On Lucene 5.3.2, If I run 
 '''java
 String[] fields = new String[]{ "field1"};
 Analyzer analyzer = new StandardAnalyzer();
 Map<String, Float> boosts = Map.of("field1", 1.5f);
 MultiFieldQueryParser parser = new MultiFieldQueryParser(fields, analyzer, boosts);
 Query query = parser.parse("\"hello 

### Sample 4 — `apache__lucene-12212`

**Files likely affected**: `lucene/facet/src/java/org/apache/lucene/facet/DrillSidewaysScorer.java`
**FAIL_TO_PASS** (1 tests, first 3): `['org.apache.lucene.facet.TestDrillSideways > testDrillSidewaysSearchUseCorrectIterator']`

**Problem statement (excerpt):**
> Searches made via DrillSideways may miss documents that should match the query. ### Description
 
 Hi,
 
 I use 'DrillSideways' quite heavily in a project of mine and it recently realized that sometimes some documents that *should* match a query do not, whenever at least one component of the 'DrillDownQuery' involved was of type 'PhraseQuery'. 
 
 This behaviour is reproducible **every** time from

### Sample 5 — `apache__lucene-12626`

**Files likely affected**: `lucene/CHANGES.txt`, `lucene/core/src/java/org/apache/lucene/index/SegmentInfos.java`
**FAIL_TO_PASS** (1 tests, first 3): `['org.apache.lucene.index.TestIndexWriter > testGetCommitDataFromOldSnapshot']`

**Problem statement (excerpt):**
> segmentInfos.replace() doesn't set userData ### Description
 
 Found that the [replace method](https://github.com/qcri/solr-6/blob/master/lucene/core/src/java/org/apache/lucene/index/SegmentInfos.java#L875-L878) doesn't set 'userData' with the new user data from 'other'. Unsure if this is an oversight, but if it is, I have a PR up [here.
 ](https://github.com/apache/lucene/pull/12626)
 
 Existing:

### Sample 6 — `apache__lucene-13170`

**Files likely affected**: `lucene/analysis/opennlp/src/java/org/apache/lucene/analysis/opennlp/OpenNLPSentenceBreakIterator.java`
**FAIL_TO_PASS** (1 tests, first 3): `['org.apache.lucene.analysis.opennlp.TestOpenNLPSentenceBreakIterator > testPrecedingWithTwoSentences']`

**Problem statement (excerpt):**
> ArrayIndexOutOfBoundsException in OpenNLPSentenceBreakIterator  ### Description  When calling [preceding ](https://github.com/apache/lucene/blob/0782535017c9e737350e96fb0f53457c7b8ecf03/lucene/analysis/opennlp/src/java/org/apache/lucene/analysis/opennlp/OpenNLPSentenceBreakIterator.java#L136) function from [OpenNLPSentenceBreakIterator](https://github.com/apache/lucene/blob/main/lucene/analysis/op

### Sample 7 — `apache__lucene-13301`

**Files likely affected**: `lucene/core/src/java/org/apache/lucene/geo/XYCircle.java`, `lucene/core/src/java/org/apache/lucene/geo/Circle.java`, `lucene/core/src/java/org/apache/lucene/geo/XYPoint.java`, `lucene/core/src/java/org/apache/lucene/geo/Point.java`, `lucene/core/src/java/org/apache/lucene/geo/Rectangle2D.java`
**FAIL_TO_PASS** (1 tests, first 3): `['org.apache.lucene.geo.TestXYPoint > testEqualsAndHashCode']`

**Problem statement (excerpt):**
> Reproducible failure in TestXYPoint.testEqualsAndHashCode ### Description  This failure is because when comparing float values using the '==' operation, '-0.0' is equal to '0.0', but their hashcode is different. should we use 'Float.compare' or 'Float.floatToRawIntBits' instead of '==' for the compare? it seems to do this change also in 'XYPoint#equals' like:
 
 '''diff
 -    return point.x == x &

### Sample 8 — `apache__lucene-13494`

**Files likely affected**: `lucene/CHANGES.txt`, `lucene/facet/src/java/org/apache/lucene/facet/StringValueFacetCounts.java`
**FAIL_TO_PASS** (1 tests, first 3): `['TestStringValueFacetCounts > testEmptyMatchset']`

**Problem statement (excerpt):**
> NullPointerException in StringValueFacetCounts when using MultiCollectorManager ### Description  When I use 'MultiCollectorManager' which merges both 'FacetsCollectorManager' and 'TopScoreDocCollectorManager' with a query not matching any docs, I expect to get '0' as a facet count, but get NPE:
 
 '''
 Cannot read the array length because "this.denseCounts" is null
 java.lang.NullPointerException:

## Section 6 — Builder guidance

When building a fix for an instance in apache/lucene:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. lucene/CHANGES.txt appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 9 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "apache/lucene"`).

First 20 instance_ids:

- `apache__lucene-11760` (dataset: `swe-bench-multilingual-test`)
- `apache__lucene-12022` (dataset: `swe-bench-multilingual-test`)
- `apache__lucene-12196` (dataset: `swe-bench-multilingual-test`)
- `apache__lucene-12212` (dataset: `swe-bench-multilingual-test`)
- `apache__lucene-12626` (dataset: `swe-bench-multilingual-test`)
- `apache__lucene-13170` (dataset: `swe-bench-multilingual-test`)
- `apache__lucene-13301` (dataset: `swe-bench-multilingual-test`)
- `apache__lucene-13494` (dataset: `swe-bench-multilingual-test`)
- `apache__lucene-13704` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
