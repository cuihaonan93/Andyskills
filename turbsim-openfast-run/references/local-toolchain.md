# Verified Local Toolchain

Verified on 2026-08-22. Recheck before relying on these values.

## Binaries

- OpenFAST:
  `C:\Users\15382\Desktop\Wind\CL_ROSCO\references\OpenFAST.exe`
  - Version: OpenFAST v5.0.0
  - Build: 64-bit, single precision
  - SHA-256: `3A7CB8EDBE10E4BCC2B048377F4FA7CA2CB906A78265E01C25AB94929C265E42`
- TurbSim:
  `C:\Users\15382\Desktop\Wind\CL_ROSCO\references\openfast-5.0.0\reg_tests\r-test\glue-codes\openfast\5MW_Baseline\Wind\TurbSim.exe`
  - Version: TurbSim v5.0.0
  - Build: 64-bit, single precision
  - SHA-256: `95C0B8867E2B2F322899975229E2B4358E88F2DDC26F1DEFD19504451C80DFE0`
- Downloaded controller DLL (not verified as ROSCO):
  `C:\Users\15382\Desktop\Wind\CL_ROSCO\references\DISCON.dll`
  - SHA-256: `A2501ADA8494C665C3A2AE6AA287A646DD2465CE4AB8C751998A47CF6A9BA548`
- DLL inside the ROSCO checkout (not verified as ROSCO):
  `C:\Users\15382\Desktop\Wind\CL_ROSCO\references\ROSCO\rosco\lib\libdiscon.dll`
  - SHA-256: `468F8DF572E6BCDC05D476609545F8B9CA70CD5F1813101795ABD90CCA9D6CDB`

Both listed DLLs initialize when the specified `DISCON.IN` is missing and return
the traditional NREL 5 MW controller message. Neither is approved for ROSCO
experiments. The checkout reports package version 2.10.4 but its generated
controller source reports 2.10.1; these values do not prove either DLL's identity.
Obtain or build a controller from a pinned ROSCO release, preserve artifact
provenance, verify configuration-file rejection/acceptance behavior, and pair it
with a turbine-specific `DISCON.IN`.

## Reference Sources

- OpenFAST 5.0.0 source and regression cases:
  `C:\Users\15382\Desktop\Wind\CL_ROSCO\references\openfast-5.0.0`
- ROSCO:
  `C:\Users\15382\Desktop\Wind\CL_ROSCO\references\ROSCO`
- WEIS:
  `C:\Users\15382\Desktop\Wind\CL_ROSCO\references\WEIS-main`
- Deprecated but locally available pyFAST toolbox:
  `C:\Users\15382\Desktop\Wind\CL_ROSCO\references\python-toolbox`
- Research Python:
  `C:\Users\15382\anaconda3\envs\StudyPyTorch\python.exe`

The correct directory segment is `CL_ROSCO`, not `CL\_ROSCO`.

## Minimum Case Manifest

Record turbine ID, case ID, input directory, all source hashes, binary hashes,
TurbSim seed and parameters, OpenFAST time step/duration, controller identity,
enabled modules, output channels, timestamps, command lines, exit codes, and paths
to stdout/stderr and produced files.
