---
name: swebench-mrdoob__three.js
description: SWE-bench repo behavioral spec for mrdoob/three.js. Aggregated from 3 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# mrdoob/three.js — SWE-bench Repo Spec

> **3 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 3 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/loaders/ObjectLoader.js` | 1 |
| `src/core/Object3D.js` | 1 |
| `src/objects/Mesh.js` | 1 |
| `src/objects/Points.js` | 1 |
| `src/objects/Line.js` | 1 |
| `src/math/Sphere.js` | 1 |
| `docs/api/zh/math/Sphere.html` | 1 |
| `docs/api/it/math/Sphere.html` | 1 |
| `docs/api/en/math/Sphere.html` | 1 |
| `docs/api/ar/math/Sphere.html` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: Core > Object3D > toJSON, Objects > Line > copy/material, Objects > Mesh > copy/material, Objects > Points > copy/material, Maths > Sphere > isSphere**

Sample FAIL_TO_PASS test names (first 10):
```
  Core > Object3D > toJSON
  Objects > Line > copy/material
  Objects > Mesh > copy/material
  Objects > Points > copy/material
  Maths > Sphere > isSphere
```

## Section 4 — Problem-theme distribution

Top themes across 3 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| json_serialization | 1 | 33.3% |
| performance | 1 | 33.3% |
| other | 1 | 33.3% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `mrdoob__three.js-25687`

**Files likely affected**: `src/loaders/ObjectLoader.js`, `src/core/Object3D.js`
**FAIL_TO_PASS** (1 tests, first 3): `['Core > Object3D > toJSON']`

**Problem statement (excerpt):**
> Serialization of PerspectiveCamera ### Description  When serializing a PerspectiveCamera and deserializing it with ObjectLoader the up-vector is not set correctly. Maybe I am missing something?
   ### Reproduction steps  1. create a PerspectiveCamera where the up-vector is not the default (0,1,0)
 2. serialize the camera and deserialize it with ObjectLoader
 3. the deserialized camera now has the 

### Sample 2 — `mrdoob__three.js-26589`

**Files likely affected**: `src/objects/Mesh.js`, `src/objects/Points.js`, `src/objects/Line.js`
**FAIL_TO_PASS** (3 tests, first 3): `['Objects > Line > copy/material', 'Objects > Mesh > copy/material', 'Objects > Points > copy/material']`

**Problem statement (excerpt):**
> Clone the material array when Object3D.clone() is called ### Description  I get that cloning the materials themselves doesn't make sense. This would be a big performance hit.
 But the materials array seems like it is part of the object to me. So if I call 'Object3D.clone()', I'd expect that array to get cloned as well.
 Sharing material references between objects makes sense. But sharing the same 

### Sample 3 — `mrdoob__three.js-27395`

**Files likely affected**: `src/math/Sphere.js`, `docs/api/zh/math/Sphere.html`, `docs/api/it/math/Sphere.html`, `docs/api/en/math/Sphere.html`, `docs/api/ar/math/Sphere.html`
**FAIL_TO_PASS** (1 tests, first 3): `['Maths > Sphere > isSphere']`

**Problem statement (excerpt):**
> Class Sphere is missing property isSphere ### Description  Box3 has this.isBox3 = true;
 Sphere does not have this.isSphere;  ### Reproduction steps  I need it for 
 if(collider.isSphere)  ### Code  a = new Sphere()
 if(a.isSphere){ debugger }  ### Live example  no example  ### Screenshots  _No response_  ### Version  r159  ### Device  _No response_  ### Browser  _No response_  ### OS  _No respons

## Section 6 — Builder guidance

When building a fix for an instance in mrdoob/three.js:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/loaders/ObjectLoader.js appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 3 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "mrdoob/three.js"`).

First 20 instance_ids:

- `mrdoob__three.js-25687` (dataset: `swe-bench-multilingual-test`)
- `mrdoob__three.js-26589` (dataset: `swe-bench-multilingual-test`)
- `mrdoob__three.js-27395` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
