# Dynamics Validation

## Matching Conditions

Use the same turbine, enabled modules, controller/actuator configuration, operating
point, coordinates, units, state ordering, and perturbation convention. Record
whether the comparison is continuous or discrete time and the discretization used.

## Comparisons

- Eigenfrequency and damping ratio.
- Pole location and stability margin.
- Mode shape correlation, such as MAC, where states are comparable.
- Input/output frequency response magnitude and phase.
- Learned-model Jacobians with respect to state and commands.
- Variation of modes across wind speed, rotor speed, pitch, and turbine design.

## Interpretation

A time-series fit can hide incorrect modes; a local modal fit can hide global
nonlinear error. Require both local dynamics validation and nonlinear free rollout.
For latent models with unmatched state coordinates, prioritize input/output transfer
behavior and observable modes over direct latent-state equality.
