# Dataset Schema

## Case Manifest

Required fields:

- `schema_version`, `case_id`, `turbine_id`, and `turbine_family`.
- OpenFAST, TurbSim, ROSCO, parser, and model-interface versions/hashes.
- Paths and SHA-256 hashes for source inputs, wind files, controller DLL, and
  `DISCON.IN`.
- Enabled OpenFAST modules and structural/control topology.
- Simulation start, discard/transient interval, time step, duration, and seed.
- Operating condition and split assignment.
- Channel records with source name, semantic name, role, unit, sign convention,
  frame, sample rate, and availability mask.

## Channel Roles

Assign every channel exactly one primary causal role:

- `exogenous`: wind, waves, environmental disturbances.
- `command`: pitch, torque, yaw, flap, or other actuator commands sent by ROSCO.
- `measurement`: signals available to ROSCO or an observer at the current time.
- `target`: engineering response to reproduce but not necessarily observe online.
- `descriptor`: static turbine, module, or controller context.
- `state_hint`: optional simulated state used for analysis, never assumed measurable.

## Alignment

Document whether commands are applied at `k` or `k+1`, controller and plant sample
times, zero-order holds, delays, filtering, and rate/position saturation. Store raw
and aligned data separately.

## Cross-Turbine Normalization

Fit normalization on training turbines only. Prefer dimensionless or physically
scaled quantities when valid, but retain native units. Store scale parameters and
masks so a new turbine can be processed without test-set leakage.
