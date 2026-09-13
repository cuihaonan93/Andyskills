---
name: wind-plant-model-train
description: Build and train causal, turbine-conditioned dynamic plant models from OpenFAST or operating data using CUDA. Use for baseline selection, model interfaces, sequence sampling, multi-step losses, cross-turbine training, checkpointing, adaptation, ablations, and reproducible experiments. Do not train a controller or evaluate fidelity only with teacher forcing.
---

# Wind-Plant Model Training

Train a plant model whose causal inputs are exogenous excitation, actuator commands,
turbine context, and available history/state. ROSCO is external to the learned model.

Read [references/training-contract.md](references/training-contract.md) before
choosing an architecture, sampler, loss, or adaptation protocol.

## Workflow

1. Freeze the dataset schema, turbine-level splits, alignment, normalization, and
   supported channel set using `$openfast-io`.
2. Establish persistence, linear state-space/subspace, and at least one simple
   nonlinear dynamic baseline before introducing a more complex architecture.
3. Define a common plant interface so every model receives identical information
   and produces the same measurement/target schema.
4. Train with CUDA using the absolute StudyPyTorch interpreter. Log data/config/code
   hashes, seeds, environment, model size, optimizer state, and normalization.
5. Use scheduled multi-step free-rollout objectives in addition to one-step loss.
   Balance channels in physical or declared dimensionless scales.
6. Select checkpoints only on validation turbines/cases. Never tune against the
   held-out test turbines.
7. Run ablations for turbine descriptors, calibration context, command inputs,
   physics constraints, and rollout loss.
8. Hand checkpoints to `$openfast-postpro`, `$openfast-linearize`, and
   `$rosco-plant-loop` for independent evaluation.

## Model Choice

Keep architecture selection open and evidence-driven. Specific model families are
research hypotheses, not defaults. Adopt a more complex architecture only when it
improves unseen-turbine free rollout, dynamics, adaptation, uncertainty, or compute
cost under a comparable experimental budget.

## Safety And Reproducibility

- Default to `--device cuda`; reduce batch/sequence size on OOM before CPU fallback.
- Preserve the last resumable checkpoint separately from the best validation model.
- Detect NaN/Inf, exploding gradients, unstable rollouts, and physical-limit
  violations during training, not only after it.
- Never modify raw datasets or reference OpenFAST/ROSCO repositories from training.
