---
name: swebench-hashicorp__terraform
description: SWE-bench repo behavioral spec for hashicorp/terraform. Aggregated from 5 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# hashicorp/terraform — SWE-bench Repo Spec

> **5 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `internal/terraform/transform_attach_config_resource.go` | 2 |
| `internal/command/fmt.go` | 1 |
| `internal/builtin/provisioners/remote-exec/resource_provisioner.go` | 1 |
| `internal/terraform/node_resource_abstract_instance.go` | 1 |
| `internal/terraform/marks.go` | 1 |
| `internal/terraform/node_resource_plan_partialexp.go` | 1 |
| `internal/terraform/node_resource_plan.go` | 1 |
| `internal/terraform/context_validate.go` | 1 |
| `internal/terraform/graph_builder_plan.go` | 1 |
| `internal/terraform/node_resource_validate.go` | 1 |
| `internal/terraform/eval_import.go` | 1 |
| `internal/terraform/transform_config.go` | 1 |
| `internal/terraform/eval_for_each.go` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: TestFmt_MockDataFiles, TestFmt_MockDataFiles/data, TestFmt_MockDataFiles/resource, TestProvisionerTimeout, TestContext2Apply_sensitiveNestedComputedAttributes**

Sample FAIL_TO_PASS test names (first 10):
```
  TestFmt_MockDataFiles
  TestFmt_MockDataFiles/data
  TestFmt_MockDataFiles/resource
  TestProvisionerTimeout
  TestContext2Apply_sensitiveNestedComputedAttributes
  TestContext2Plan_nestedSensitiveMarks
  TestContext2Plan_importResourceConfigGenExpandedResource
  TestContext2Plan_importGenerateNone
  TestContext2Plan_importSelfReference
  TestContext2Plan_importSelfReferenceInstanceRef
```

## Section 4 — Problem-theme distribution

Top themes across 5 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| config_environment | 3 | 60.0% |
| other | 1 | 20.0% |
| wrong_output | 1 | 20.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `hashicorp__terraform-34580`

**Files likely affected**: `internal/command/fmt.go`
**FAIL_TO_PASS** (3 tests, first 3): `['TestFmt_MockDataFiles', 'TestFmt_MockDataFiles/data', 'TestFmt_MockDataFiles/resource']`

**Problem statement (excerpt):**
> 'terraform fmt' does not handle '.tfmock.hcl' files ### Terraform Version
 
 '''shell
 Terraform v1.7.1
 '''
 
 
 ### Use Cases
 
 When using the Terraform 1.7 mocks feature as suggested in the official tutorial: https://developer.hashicorp.com/terraform/language/tests/mocking#mock-provider-data
 
 Terraform formatting does not apply to the '.tfmock.hcl' files
 
 '''shell
 terraform fmt tests/aws/

### Sample 2 — `hashicorp__terraform-34814`

**Files likely affected**: `internal/builtin/provisioners/remote-exec/resource_provisioner.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestProvisionerTimeout']`

**Problem statement (excerpt):**
> SSH connections are kept open ### Terraform Version  '''shell Terraform v1.6.2
 on linux_amd64
 + provider registry.terraform.io/hashicorp/null v3.1.1 '''   ### Terraform Configuration Files  '''terraform
 terraform {
   required_version = "~> 1.1"
   required_providers {
     null = {
       source  = "hashicorp/null"
       version = "~> 3.1.1"
     }
   }
 }
 
 variable "host" {
   type = strin

### Sample 3 — `hashicorp__terraform-34900`

**Files likely affected**: `internal/terraform/node_resource_abstract_instance.go`, `internal/terraform/marks.go`, `internal/terraform/node_resource_plan_partialexp.go`
**FAIL_TO_PASS** (2 tests, first 3): `['TestContext2Apply_sensitiveNestedComputedAttributes', 'TestContext2Plan_nestedSensitiveMarks']`

**Problem statement (excerpt):**
> Set nested block with sensitive attribute always detects changes on 'v1.8.0-rc1' ### Terraform Version  '''shell Terraform v1.8.0-rc1
 on darwin_arm64 '''   ### Terraform Configuration Files  '''terraform
 terraform {
   required_providers {
     examplecloud = {
       source = "austinvalle/sandbox"
     }
   }
 }
 
 resource "examplecloud_thing" "test" {
   set_nested_block {
     sensitive_str 

### Sample 4 — `hashicorp__terraform-35543`

**Files likely affected**: `internal/terraform/node_resource_plan.go`, `internal/terraform/context_validate.go`, `internal/terraform/graph_builder_plan.go`, `internal/terraform/node_resource_validate.go`, `internal/terraform/eval_import.go`
**FAIL_TO_PASS** (6 tests, first 3): `['TestContext2Plan_importResourceConfigGenExpandedResource', 'TestContext2Plan_importGenerateNone', 'TestContext2Plan_importSelfReference']`

**Problem statement (excerpt):**
> terraform validate does not validate import blocks ### Terraform Version  '''shell Terraform v1.9.3
 on linux_amd64 '''   ### Terraform Configuration Files  '''terraform
 resource "null_resource" "undef-local" {
 }
 
 resource "null_resource" "undef-var" {
 }
 
 import {
   to = null_resource.undef-local
   id = local.something_not_defined
 }
 
 import {
   to = null_resource.undef-var
   id = var

### Sample 5 — `hashicorp__terraform-35611`

**Files likely affected**: `internal/terraform/transform_attach_config_resource.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestContext2Apply_provisionerDestroyRemoved']`

**Problem statement (excerpt):**
> When using "module", local-exec commands written in "removed block" are not executed ### Terraform Version  '''shell Terraform v1.9.4
 on darwin_arm64
 + provider registry.terraform.io/hashicorp/null v3.2.2 '''   ### Terraform Configuration Files  This is 'main.tf' file.
 '''terraform
 terraform {
   backend "local" {
   }
 }
 
 removed {
   from = module.null.null_resource.main
   provisioner "lo

## Section 6 — Builder guidance

When building a fix for an instance in hashicorp/terraform:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. internal/terraform/transform_attach_config_resource.go appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 5 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "hashicorp/terraform"`).

First 20 instance_ids:

- `hashicorp__terraform-34580` (dataset: `swe-bench-multilingual-test`)
- `hashicorp__terraform-34814` (dataset: `swe-bench-multilingual-test`)
- `hashicorp__terraform-34900` (dataset: `swe-bench-multilingual-test`)
- `hashicorp__terraform-35543` (dataset: `swe-bench-multilingual-test`)
- `hashicorp__terraform-35611` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
