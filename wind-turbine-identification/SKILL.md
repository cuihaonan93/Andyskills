---
name: wind-turbine-identification
description: Orchestrate turbine-agnostic, data-driven identification of wind-turbine plant dynamics from OpenFAST or operating data. Use for research design, dataset contracts, cross-turbine generalization, model training, open-loop validation, or same-ROSCO closed-loop equivalence. Do not use to replace ROSCO with a learned controller.
---

# Wind-Turbine Plant Identification

Treat the learned system as the wind-turbine **plant**. Keep wind/exogenous inputs,
ROSCO, actuator commands, plant states, measurements, and engineering outputs as
separate causal objects.

## Route The Work

- Generate TurbSim wind and OpenFAST cases with `$turbsim-openfast-run`.
- Parse inputs, outputs, channels, units, and manifests with `$openfast-io`.
- Build and train causal turbine-conditioned plants with
  `$wind-plant-model-train`.
- Compare local modes and operating-point dynamics with `$openfast-linearize`.
- Evaluate time series, spectra, loads, and DEL with `$openfast-postpro`.
- Connect the identical ROSCO implementation to both plants with
  `$rosco-plant-loop`.

Read [references/research-contract.md](references/research-contract.md) when
designing a dataset, model interface, experiment, or acceptance gate.

## Non-Negotiable Boundaries

1. The model must consume exogenous inputs and actuator commands. A model trained
   only on wind and closed-loop responses learns a controller-dependent mapping,
   not a replaceable plant.
2. Split by complete turbine design before window generation. A cross-turbine claim
   requires turbines absent from training, not merely unseen time ranges.
3. Condition the shared identifier on available turbine descriptors, module
   topology, controller metadata, channel semantics, and a finite calibration
   trajectory. Represent missing information explicitly.
4. Evaluate multi-step free rollout. Teacher-forced one-step error is diagnostic,
   not open-loop validation.
5. State the supported turbine family, topology, operating envelope, observation
   set, and adaptation budget. Do not claim literal universality from finite data.
6. Keep reference repositories and binaries read-only. Generate cases and results
   in a separate experiment workspace.

## Stage Gates

Proceed in this order:

1. Verify toolchain versions and hashes.
2. Prove one reproducible TurbSim -> OpenFAST -> ROSCO -> output case.
3. Freeze channel semantics, case manifest, and turbine-level data split.
4. Establish simple linear/state-space and persistence baselines.
5. Train the identified plant on CUDA and test free rollout.
6. Validate modes, spectra, loads, stability, and uncertainty.
7. Close the same ROSCO around the identified plant.
8. Test unseen turbines with zero-shot and declared few-shot adaptation.
