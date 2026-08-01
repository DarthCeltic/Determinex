# Family: benchmark_timing  [v1 stub]

> Generator: `wave3/benchmark_timing/scaffold_generator.py` → uses `generator_lib.FAMILY_SPECS["benchmark_timing"]`

## Behavior

See FAMILY_SPECS entry in `corpus/programbench/families/generator_lib.py`.
This family currently emits a v1 scaffold that:
- recognizes the family's typical flag matrix
- emits help with the family description
- handles file arguments + stdin
- exits with clap-style errors (rc=2 on unknown flag)

## Refinement plan

When a tool in this family gets sprint focus, fill in this FAMILY.md with:
1. Tests-the-family-typically-faces (probe `mass_run_v2_base/<instance>/<iid>.eval.json`)
2. Common flags table (refined from generator_lib defaults)
3. Error conventions (rc codes + wordings)
4. Known traps (from per-tool v1 → v2 lessons)

## Exemplar tools

None locked yet. Sprint-4 bulk-generation populates first candidates.
