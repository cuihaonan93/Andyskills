---
name: openfast-io
description: Read and write OpenFAST, TurbSim, and linearization files and build unit-aware, provenance-preserving datasets from .out, .outb, .dat, .fst, .bts, and .lin data. Use for channel discovery, safe input edits, conversion, schemas, manifests, and cross-turbine alignment. Do not guess field names or overwrite reference inputs.
---

# OpenFAST Data I/O

Use structured parsers before custom text parsing. The local legacy toolbox is at
`C:\Users\15382\Desktop\Wind\CL_ROSCO\references\python-toolbox` and exposes
`pyFAST.input_output`, including `FASTInputFile`, `FASTOutputFile`,
`TurbSimFile`, and `FASTLinearizationFile`.

## Workflow

1. Inspect the actual file and parser-supported fields before editing.
2. Preserve raw channel names and units; create semantic aliases separately.
3. Write changed inputs to an experiment copy with a new filename.
4. Attach turbine, case, source hash, sample interval, controller, and split metadata.
5. Validate monotonic time, duplicate channels, missing values, unit consistency,
   finite values, and expected sample counts.
6. Split complete cases and turbine IDs before creating windows or normalization
   statistics.

Read [references/dataset-schema.md](references/dataset-schema.md) when producing a
training dataset or defining the learned plant interface.

## Boundaries

- The downloaded `python-toolbox` is deprecated pyFAST. Use it for reproducibility
  with this local source, but do not conflate it with the current `openfast-io`
  package used by modern ROSCO.
- Do not silently interpolate, resample, rename, or convert units. Record each
  transformation and its parameters.
- Distinguish unavailable channels, disabled-module channels, and missing samples.
- Keep future outputs out of inputs and normalization. Preserve causal alignment
  between wind, commands, measurements, and targets.
