---
name: swebench-scikit-learn__scikit-learn
description: SWE-bench repo behavioral spec for scikit-learn/scikit-learn. Aggregated from 284 bug-fix instances across 3 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# scikit-learn/scikit-learn — SWE-bench Repo Spec

> **284 bug-fix instances** across 3 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-test | 229 |
| swe-bench-verified-test | 32 |
| swe-bench-lite-test | 23 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `sklearn/linear_model/logistic.py` | 12 |
| `sklearn/compose/_column_transformer.py` | 12 |
| `sklearn/feature_extraction/text.py` | 11 |
| `sklearn/utils/estimator_checks.py` | 11 |
| `sklearn/utils/validation.py` | 10 |
| `sklearn/linear_model/ridge.py` | 9 |
| `sklearn/preprocessing/_encoders.py` | 9 |
| `sklearn/model_selection/_search.py` | 9 |
| `sklearn/pipeline.py` | 8 |
| `sklearn/svm/base.py` | 8 |
| `sklearn/model_selection/_split.py` | 8 |
| `sklearn/base.py` | 8 |
| `sklearn/metrics/classification.py` | 8 |
| `sklearn/preprocessing/data.py` | 8 |
| `sklearn/metrics/pairwise.py` | 7 |
| `sklearn/mixture/base.py` | 6 |
| `sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py` | 6 |
| `sklearn/linear_model/coordinate_descent.py` | 6 |
| `sklearn/calibration.py` | 6 |
| `sklearn/ensemble/iforest.py` | 5 |
| `sklearn/ensemble/voting.py` | 5 |
| `sklearn/impute/_iterative.py` | 5 |
| `sklearn/metrics/_ranking.py` | 5 |
| `sklearn/impute.py` | 5 |
| `sklearn/utils/_show_versions.py` | 4 |
| `sklearn/multioutput.py` | 4 |
| `sklearn/feature_selection/_base.py` | 4 |
| `sklearn/model_selection/_validation.py` | 4 |
| `sklearn/ensemble/gradient_boosting.py` | 4 |
| `sklearn/preprocessing/label.py` | 3 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  sklearn/linear_model/tests/test_ridge.py::test_ridge_classifier_cv_store_cv_values
  sklearn/preprocessing/tests/test_label.py::test_label_encoder_errors
  sklearn/preprocessing/tests/test_label.py::test_label_encoder_empty_array
  sklearn/utils/tests/test_validation.py::test_check_dataframe_warns_on_dtype
  sklearn/neighbors/tests/test_neighbors.py::test_n_neighbors_datatype
  sklearn/mixture/tests/test_bayesian_mixture.py::test_bayesian_mixture_fit_predict
  sklearn/mixture/tests/test_gaussian_mixture.py::test_gaussian_mixture_fit_predict
  sklearn/preprocessing/tests/test_encoders.py::test_one_hot_encoder_handle_unknown_strings
  sklearn/mixture/tests/test_bayesian_mixture.py::test_bayesian_mixture_fit_predict_n_init
  sklearn/mixture/tests/test_gaussian_mixture.py::test_gaussian_mixture_fit_predict_n_init
```

## Section 4 — Problem-theme distribution

Top themes across 284 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 112 | 39.4% |
| regression | 40 | 14.1% |
| import_module | 37 | 13.0% |
| wrong_output | 25 | 8.8% |
| documentation | 22 | 7.7% |
| crash_or_traceback | 14 | 4.9% |
| edge_case | 12 | 4.2% |
| type_handling | 6 | 2.1% |
| config_environment | 5 | 1.8% |
| performance | 4 | 1.4% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `scikit-learn__scikit-learn-10297`

**Files likely affected**: `sklearn/linear_model/ridge.py`
**FAIL_TO_PASS** (1 tests, first 3): `['sklearn/linear_model/tests/test_ridge.py::test_ridge_classifier_cv_store_cv_values']`

**Problem statement (excerpt):**
> linear_model.RidgeClassifierCV's Parameter store_cv_values issue #### Description
 Parameter store_cv_values error on sklearn.linear_model.RidgeClassifierCV
 
 #### Steps/Code to Reproduce
 import numpy as np
 from sklearn import linear_model as lm
 
 #test database
 n = 100
 x = np.random.randn(n, 30)
 y = np.random.normal(size = n)
 
 rr = lm.RidgeClassifierCV(alphas = np.arange(0.1, 1000, 0.1),

### Sample 2 — `scikit-learn__scikit-learn-10508`

**Files likely affected**: `sklearn/preprocessing/label.py`
**FAIL_TO_PASS** (2 tests, first 3): `['sklearn/preprocessing/tests/test_label.py::test_label_encoder_errors', 'sklearn/preprocessing/tests/test_label.py::test_label_encoder_empty_array']`

**Problem statement (excerpt):**
> LabelEncoder transform fails for empty lists (for certain inputs) Python 3.6.3, scikit_learn 0.19.1
 
 Depending on which datatypes were used to fit the LabelEncoder, transforming empty lists works or not. Expected behavior would be that empty arrays are returned in both cases.
 
 '''python
 >>> from sklearn.preprocessing import LabelEncoder
 >>> le = LabelEncoder()
 >>> le.fit([1,2])
 LabelEncode

### Sample 3 — `scikit-learn__scikit-learn-10949`

**Files likely affected**: `sklearn/utils/validation.py`
**FAIL_TO_PASS** (1 tests, first 3): `['sklearn/utils/tests/test_validation.py::test_check_dataframe_warns_on_dtype']`

**Problem statement (excerpt):**
> warn_on_dtype with DataFrame #### Description
 
 ''warn_on_dtype'' has no effect when input is a pandas ''DataFrame''
 
 #### Steps/Code to Reproduce
 '''python
 from sklearn.utils.validation import check_array
 import pandas as pd
 df = pd.DataFrame([[1, 2, 3], [2, 3, 4]], dtype=object)
 checked = check_array(df, warn_on_dtype=True)
 '''
 
 #### Expected result: 
 
 '''python-traceback
 DataConve

### Sample 4 — `scikit-learn__scikit-learn-11040`

**Files likely affected**: `sklearn/neighbors/base.py`
**FAIL_TO_PASS** (1 tests, first 3): `['sklearn/neighbors/tests/test_neighbors.py::test_n_neighbors_datatype']`

**Problem statement (excerpt):**
> Missing parameter validation in Neighbors estimator for float n_neighbors '''python
 from sklearn.neighbors import NearestNeighbors
 from sklearn.datasets import make_blobs
 X, y = make_blobs()
 neighbors = NearestNeighbors(n_neighbors=3.)
 neighbors.fit(X)
 neighbors.kneighbors(X)
 '''
 '''
 ~/checkout/scikit-learn/sklearn/neighbors/binary_tree.pxi in sklearn.neighbors.kd_tree.NeighborsHeap.__ini

### Sample 5 — `scikit-learn__scikit-learn-11281`

**Files likely affected**: `sklearn/mixture/base.py`
**FAIL_TO_PASS** (2 tests, first 3): `['sklearn/mixture/tests/test_bayesian_mixture.py::test_bayesian_mixture_fit_predict', 'sklearn/mixture/tests/test_gaussian_mixture.py::test_gaussian_mixture_fit_predict']`

**Problem statement (excerpt):**
> Should mixture models have a clusterer-compatible interface Mixture models are currently a bit different. They are basically clusterers, except they are probabilistic, and are applied to inductive problems unlike many clusterers. But they are unlike clusterers in API:
 * they have an 'n_components' parameter, with identical purpose to 'n_clusters'
 * they do not store the 'labels_' of the training

### Sample 6 — `scikit-learn__scikit-learn-12471`

**Files likely affected**: `sklearn/preprocessing/_encoders.py`
**FAIL_TO_PASS** (1 tests, first 3): `['sklearn/preprocessing/tests/test_encoders.py::test_one_hot_encoder_handle_unknown_strings']`

**Problem statement (excerpt):**
> OneHotEncoder ignore unknown error when categories are strings  #### Description
 
 This bug is very specific, but it happens when you set OneHotEncoder to ignore unknown entries.
 and your labels are strings. The memory of the arrays is not handled safely and it can lead to a ValueError
 
 Basically, when you call the transform method it will sets all the unknown strings on your array to OneHotEn

### Sample 7 — `scikit-learn__scikit-learn-13142`

**Files likely affected**: `sklearn/mixture/base.py`
**FAIL_TO_PASS** (2 tests, first 3): `['sklearn/mixture/tests/test_bayesian_mixture.py::test_bayesian_mixture_fit_predict_n_init', 'sklearn/mixture/tests/test_gaussian_mixture.py::test_gaussian_mixture_fit_predict_n_init']`

**Problem statement (excerpt):**
> GaussianMixture predict and fit_predict disagree when n_init>1 #### Description
 When 'n_init' is specified in GaussianMixture, the results of fit_predict(X) and predict(X) are often different.  The 'test_gaussian_mixture_fit_predict' unit test doesn't catch this because it does not set 'n_init'.
 
 #### Steps/Code to Reproduce
 '''
 python
 from sklearn.mixture import GaussianMixture
 from sklear

### Sample 8 — `scikit-learn__scikit-learn-13241`

**Files likely affected**: `sklearn/decomposition/kernel_pca.py`
**FAIL_TO_PASS** (1 tests, first 3): `['sklearn/decomposition/tests/test_kernel_pca.py::test_kernel_pca_deterministic_output']`

**Problem statement (excerpt):**
> Differences among the results of KernelPCA with rbf kernel Hi there,
 I met with a problem:
 
 #### Description
 When I run KernelPCA for dimension reduction for the same datasets, the results are different in signs.
 
 #### Steps/Code to Reproduce
 Just to reduce the dimension to 7 with rbf kernel:
 pca = KernelPCA(n_components=7, kernel='rbf', copy_X=False, n_jobs=-1)
 pca.fit_transform(X)
 
 ##

## Section 6 — Builder guidance

When building a fix for an instance in scikit-learn/scikit-learn:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. sklearn/linear_model/logistic.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 284 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "scikit-learn/scikit-learn"`).

First 20 instance_ids:

- `scikit-learn__scikit-learn-10297` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-10508` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-10949` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-11040` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-11281` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-12471` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-13142` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-13241` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-13439` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-13496` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-13497` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-13584` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-13779` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-14087` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-14092` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-14894` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-14983` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-15512` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-15535` (dataset: `swe-bench-lite-test`)
- `scikit-learn__scikit-learn-25500` (dataset: `swe-bench-lite-test`)
- ... (264 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*

---

## Section 8 — Anchor-grade hand-curated reference (top-4 by instance count, 284 instances)

### Repo overview
scikit-learn is the canonical Python ML library. Bug fixes touch estimators, transformers,
metrics, and model_selection. Strict on numerical reproducibility and API consistency.

### High-leverage bug zones

| Subsystem | Touch count | Common bug pattern |
|-----------|------------|--------------------|
| `sklearn/linear_model/logistic.py` | 12 | Solver selection; multiclass strategy; sample_weight |
| `sklearn/compose/_column_transformer.py` | 12 | Column selection; remainder handling; feature names |
| `sklearn/feature_extraction/text.py` | 11 | TfidfVectorizer / CountVectorizer edge cases |
| `sklearn/utils/validation.py` | ~10 | Input validation; check_array dtype handling |
| `sklearn/model_selection/_split.py` | ~10 | KFold / StratifiedKFold edge cases (n_splits=1, empty groups) |
| `sklearn/preprocessing/_encoders.py` | ~10 | OneHotEncoder unknown categories handling |

### Test framework
**pytest** with sklearn's own `sklearn.utils._testing` helpers. FAIL_TO_PASS names look like:
`sklearn/linear_model/tests/test_logistic.py::test_predict_proba_consistency`.

### Builder rules specific to scikit-learn

1. **fit/transform/predict contract**: every estimator MUST follow it. Don't shortcut.
2. **`_validate_data` first**: in `fit()` and `predict()`, call `self._validate_data(...)` for dtype/shape checks.
3. **`sample_weight` propagation**: many fixes are about `sample_weight=None` defaults vs explicit `np.ones(n)`.
4. **Random state**: `check_random_state(self.random_state)` in `fit()`. Never use bare `np.random`.
5. **Numerical stability**: `from sklearn.utils.extmath import softmax`, `safe_sparse_dot` — use these instead of raw numpy where available.
6. **Sparse matrix support**: every transformer needs to handle both dense and sparse. Check `scipy.sparse.issparse(X)`.
7. **`feature_names_in_`** attribute: set in `fit()` if X is a DataFrame; tests assert this.

### Where 90→100% lives

- `test_*logistic*` → multinomial vs OvR; sag/saga solver convergence
- `test_*column_transformer*` → remainder='drop' vs 'passthrough'; output dtype
- `test_*tfidf*` → IDF weighting; max_features tie-breaking
- `test_*split*` → stratified groups; small-N edge cases
- `test_*encoder*` → unknown handling; sparse output

### Estimated lock cost per instance
~8-18 min on Sonnet; ~25-45 min on local Qwen 14b. Numerical correctness requires careful test-driving.
