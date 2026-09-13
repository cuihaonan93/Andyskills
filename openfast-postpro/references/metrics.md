# Evaluation Metrics

## Time Domain

Report native-unit RMSE/MAE, normalized error with a declared scale, bias, peak and
peak-time error, phase lag, correlation, settling/rise time when applicable, and
quantile/distribution differences. Plot representative failures, not only median
cases.

## Frequency And Dynamics

Compare PSD, dominant frequencies, band energy, cross-spectral density, coherence,
frequency-response magnitude/phase when inputs are suitable, natural frequencies,
and damping. Use identical detrending, windows, overlap, and frequency resolution.

## Loads And Fatigue

Compare extremes and DEL using identical transient removal, rainflow convention,
Wohler exponent, reference cycle count/frequency, mean-stress treatment, and units.
State every parameter in the report.

## Stability And Physics

Measure free-rollout horizon before divergence, boundedness, NaN/Inf incidence,
energy or power-balance residuals where defined, rate/position limit violations,
and behavior outside the training envelope.

## Closed Loop

With identical ROSCO configuration, compare regulation error, overspeed, generated
power, pitch/torque activity and rate, saturation time, loads, DEL, and stability.
Closed-loop agreement does not waive open-loop plant accuracy.

## Aggregation

Use paired per-case metrics, turbine-level macro averages, bootstrap confidence
intervals over independent cases/seeds, and explicit results for unseen turbines.
Never select cases after seeing model errors.
