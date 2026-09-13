# Research Contract

## System Boundary

Reference loop:

`wind -> OpenFAST plant -> measurements -> ROSCO -> actuator commands -> plant`

Surrogate loop:

`same wind -> identified plant -> same measurements -> same ROSCO -> commands -> plant`

The identified model replaces OpenFAST only. ROSCO is not learned or replaced.

## Minimum Plant Interface

Inputs should distinguish:

- Exogenous excitation: wind-field representation, waves, and other disturbances.
- Commands: collective/individual pitch, generator torque, yaw, flaps, and other
  enabled actuators.
- Static context: turbine geometry, rated quantities, inertias, modal descriptors,
  module topology, controller/interface metadata, and channel availability.
- Dynamic context: initial state or a finite causal calibration trajectory.

Outputs should include the measurements required by ROSCO and the engineering
responses used for validation. Preserve native units and an explicit normalization
map.

## Dataset Split

Create case manifests first, then assign complete turbine IDs to train, validation,
and test sets, then create temporal windows. Within each turbine split, also hold
out operating conditions and wind seeds. Do not normalize with test-turbine data.

Report separately:

- Seen turbine, unseen wind/operating condition.
- Unseen turbine, zero-shot identification.
- Unseen turbine, few-shot adaptation with a fixed data/time budget.
- Out-of-family extrapolation, labeled as such.

## Open-Loop Gate

Replay identical exogenous excitation, actuator commands, time step, and initial
conditions through both plants. Require stable free rollout and report time-domain,
frequency-domain, modal, extreme-load, and fatigue metrics. Feedback is absent here,
so plant error cannot be hidden by ROSCO.

## Closed-Loop Gate

Use the same controller DLL, `DISCON.IN`, tuning data, interface mapping, sample
time, initialization, limits, and wind realization. Report plant-model error and
closed-loop performance separately.

## Reproducibility

Every result must trace to turbine ID, case ID, source input hashes, binary hashes,
software versions, channel/unit schema, random seeds, split assignment, model
checkpoint hash, and evaluation configuration.
