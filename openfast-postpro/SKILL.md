---
name: openfast-postpro
description: Evaluate identified wind-turbine plants against OpenFAST in open and closed loop using time-domain, frequency-domain, stability, extreme-load, and fatigue metrics. Use for .out/.outb postprocessing, plots, DEL, spectra, confidence intervals, and acceptance reports. Do not declare fidelity from aggregate RMSE alone.
---

# OpenFAST Model Evaluation

Read [references/metrics.md](references/metrics.md) before defining acceptance
criteria. Use the same cases, windows, units, initial conditions, wind realization,
and actuator commands for paired comparisons.

## Evaluation Order

1. Data integrity and initial-condition checks.
2. One-step diagnostics.
3. Multi-step open-loop free rollout with recorded commands.
4. Time-domain transient, peak, phase, and distribution comparisons.
5. PSD, cross-spectrum, coherence, and modal comparisons.
6. Extreme loads and fatigue-equivalent loads with recorded conventions.
7. Long-horizon stability and physical-constraint checks.
8. Same-ROSCO closed-loop comparison.
9. Aggregation by turbine, operating condition, and wind seed with uncertainty.

## Local Sources

- pyFAST postprocessing examples:
  `C:\Users\15382\Desktop\Wind\CL_ROSCO\references\python-toolbox\pyFAST\postpro\examples`
- WEIS notebooks:
  `C:\Users\15382\Desktop\Wind\CL_ROSCO\references\WEIS-main\examples\07_postprocessing_notebooks`

Always preserve per-case results. Report macro averages across turbines as well as
pooled values so large turbines or long cases do not dominate the conclusion.
