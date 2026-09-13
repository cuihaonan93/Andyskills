---
name: turbsim-openfast-run
description: Generate turbulent wind with the verified TurbSim 5.0 executable and run reproducible OpenFAST 5.0 simulations on Windows, including ROSCO-controlled single or batch cases. Use for toolchain checks, case generation, execution, logs, hashes, and run manifests. Do not modify reference cases in place.
---

# TurbSim And OpenFAST Runs

Use PowerShell commands and verified local binaries. Read
[references/local-toolchain.md](references/local-toolchain.md) before the first run
in a task or whenever paths or versions may have changed.

## Workflow

1. Run `scripts/check_toolchain.ps1`; stop on missing or unexpected binaries.
2. Copy the complete turbine case into a unique experiment directory. Preserve
   relative paths among `.fst`, module inputs, airfoils, controller files, and wind.
3. Generate each TurbSim `.inp` from a recorded template. Set an explicit seed,
   grid, hub height, duration, time step, turbulence model, and mean wind speed.
4. Invoke TurbSim and verify normal termination plus expected `.bts`/`.sum` files.
5. Point InflowWind to the generated wind file. Bind ServoDyn to the intended
   controller DLL and matching `DISCON.IN`.
6. Invoke OpenFAST and verify exit code, normal termination, and required outputs.
7. Write a case manifest with hashes before parsing or training.

## Execution Rules

- Run long jobs in a visible terminal where supported and report progress.
- OpenFAST and TurbSim are CPU executables; CUDA applies to model training, not
  these solvers.
- Use one isolated directory per turbine/case/seed. Never overwrite the reference
  tree or a completed case.
- Limit parallelism deliberately and capture stdout/stderr per case.
- Treat a zero exit code as necessary but insufficient: also inspect the solver log
  and output files for normal completion, NaN, or severe warnings.
- Do not invent OpenFAST field names. Use `$openfast-io` to inspect and edit inputs.

## PowerShell Forms

```powershell
& "<TurbSim.exe>" "<case.inp>"
& "<OpenFAST.exe>" "<case.fst>"
Get-Content "<case.log>" -Tail 30 -Wait
```
