---
name: openfast-linearize
description: Generate and analyze OpenFAST operating-point linearizations and compare their local dynamics with an identified wind-turbine plant. Use for A/B/C/D extraction, MBC/Campbell analysis, poles, modes, damping, local Jacobians, controller design points, and dynamics validation. Do not treat one operating-point match as global fidelity.
---

# OpenFAST Linearization

Use OpenFAST 5.0 linearization outputs and the verified local pyFAST/WEIS examples.
Read [references/dynamics-validation.md](references/dynamics-validation.md) before
comparing the learned plant to OpenFAST.

## Workflow

1. Define a steady or periodic operating point and document trim assumptions.
2. Generate enough azimuth samples when rotating coordinates require MBC analysis.
3. Parse `.lin` files with structured OpenFAST linearization tooling.
4. Apply consistent state/input/output ordering, units, frames, and operating point.
5. Compare OpenFAST dynamics with a local linearization/Jacobian of the learned
   plant at the same condition.
6. Track poles and modes across wind speeds and turbine designs; do not compare
   modes solely by sorted frequency.

## Local Sources

- pyFAST examples:
  `C:\Users\15382\Desktop\Wind\CL_ROSCO\references\python-toolbox\pyFAST\linearization\examples`
- WEIS legacy linearization:
  `C:\Users\15382\Desktop\Wind\CL_ROSCO\references\WEIS-main\examples\99_legacy_features\linearization`
- ROSCO linear parameters:
  `C:\Users\15382\Desktop\Wind\CL_ROSCO\references\ROSCO\Examples\10_linear_params.py`
