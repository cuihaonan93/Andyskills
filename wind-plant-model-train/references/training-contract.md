# Training Contract

## Causal Interface

At prediction time, the model may use only information available by that time:

- Environmental/exogenous inputs up to the current step.
- ROSCO/actuator commands under a documented timing convention.
- Static turbine and module descriptors available for the new turbine.
- A fixed causal calibration/history window or initialized latent state.

Do not leak future wind, future commands, future outputs, test-turbine normalization,
or OpenFAST-only hidden states unless the experiment explicitly studies privileged
training and removes them at inference.

## Architecture-Neutral Contract

Every candidate implements:

- State/history initialization.
- One-step transition.
- Multi-step free rollout without target feedback.
- Measurement outputs required by ROSCO.
- Engineering targets used for validation.
- Serialization of architecture, weights, context schema, and normalization.

## Losses

Combine only justified terms and report each separately:

- One-step state/output error.
- Multi-horizon free-rollout error.
- Spectral or modal error when differentiable and meaningful.
- Physical consistency or constraint penalties with defined units.
- Stability/regularization terms.

Use channel weights fixed before test evaluation. Avoid allowing high-magnitude
channels or long steady intervals to dominate transients and loads.

## Sampling

Sample turbines and cases deliberately, then temporal windows. Prevent turbines with
more simulations from dominating unless this weighting is an explicit design choice.
Include operating transitions and sufficiently exciting inputs; passive closed-loop
data alone may not identify all plant dynamics.

## Cross-Turbine Adaptation

Define zero-shot and few-shot protocols separately. For few-shot adaptation, freeze
the number/duration of calibration trajectories, trainable parameters, steps, and
compute budget. Do not use test trajectories later scored as evaluation data.

## Required Baselines And Ablations

- Persistence/last value where applicable.
- Linear state-space or subspace identification.
- A simple nonlinear recurrent/temporal model.
- Without turbine descriptors.
- Without actuator commands.
- Without calibration context/adaptation.
- Without multi-step rollout loss.

The final architecture must beat relevant baselines on unseen-turbine free rollout
and engineering dynamics, not merely training or one-step loss.
