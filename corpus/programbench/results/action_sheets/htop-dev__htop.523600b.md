# Action Sheet — htop-dev__htop.523600b

**Current:** 7.47%  (104/1393)
**Pass / Fail / Skip:** 104 / 596 / 0
**Gap to 100%:** 92.53 percentage points (1289 tests)

## Failure clusters

596 failed tests grouped into 2 buckets (sorted by count).

### `rc_mismatch_got1_want0` — 580 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_absolute_final_push.test_massive_iteration_runs`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-n', '20', '-d', '1'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 347\n    "M_NFS_UNSTABLE", "M_ML\n                    
- `tests.test_absolute_final_push.test_all_field_permutations_sample`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-n', '3'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 347\n    "M_NFS_UNSTABLE", "M_ML\n                      ^\nSyntaxE
- `tests.test_absolute_final_push.test_every_sort_with_every_direction`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-n', '5'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 347\n    "M_NFS_UNSTABLE", "M_ML\n                      ^\nSyntaxE
- *(... 577 more in this cluster)*

### `other_assertion` — 16 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_all_sorts.test_all_sort_keys_basic`
  > AssertionError: Sort key PID failed
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-n', '1', '-s', 'PID'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 347\n    "M_NFS_UNSTABLE", "M_ML\n                   
- `tests.test_coverage_boost.test_user_nonexistent`
  > assert (b'invalid' in b'  file "/workspace/main.py", line 347\n    "m_nfs_unstable", "m_ml\n                      ^\nsyntaxerror: unterminated string literal (detected at line 347)\n' or b'user' in b'
  >  +  where b'  file "/workspace/main.py", line 347\n    "m_nfs_unstable", "m_ml\n                      ^\nsyntaxerror: unterminated string literal (detected at line 347)\n' = <built-in method lower of 
  >  +    where <built-in method lower of bytes object at 0x7f9e5c3f6eb0> = b'  File "/workspace/main.py", line 347\n    "M_NFS_UNSTABLE", "M_ML\n                      ^\nSyntaxError: unterminated string 
  >  +      where b'  File "/workspace/main.py", line 347\n    "M_NFS_UNSTABLE", "M_ML\n                      ^\nSyntaxError: unterminated string literal (detected at line 347)\n' = CompletedProcess(args=
  >  +  and   b'  file "/workspace/main.py", line 347\n    "m_nfs_unstable", "m_ml\n                      ^\nsyntaxerror: unterminated string literal (detected at line 347)\n' = <built-in method lower of 
  >  +    where <built-in method lower of bytes object at 0x7f9e5c3f6eb0> = b'  File "/workspace/main.py", line 347\n    "M_NFS_UNSTABLE", "M_ML\n                      ^\nSyntaxError: unterminated string 
  >  +      where b'  File "/workspace/main.py", line 347\n    "M_NFS_UNSTABLE", "M_ML\n                      ^\nSyntaxError: unterminated string literal (detected at line 347)\n' = CompletedProcess(args=
- `tests.test_edge_cases_comprehensive.test_zero_delay`
  > assert 0 > 100
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['./executable', '-n', '5', '-d', '0'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 347\n    "M_NFS_UNSTABLE", "M_ML\n                 
- *(... 13 more in this cluster)*

