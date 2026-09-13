---
name: rosco-plant-loop
description: Connect the same ROSCO controller to OpenFAST and to an identified wind-turbine plant for interface capture, Python co-simulation, and closed-loop equivalence testing. Use for DISCON.dll/DISCON.IN pairing, avrSWAP signal maps, ControllerInterface, initialization, sample timing, actuator commands, and paired closed-loop runs. Do not train or substitute a learned controller.
---

# ROSCO Around Two Plants

The learned component is the plant. ROSCO remains the controller in both reference
and surrogate loops. Read
[references/interface-contract.md](references/interface-contract.md) before
implementing the Python loop or comparing results.

## Preferred Local Interface

Reuse the official local wrapper:

`C:\Users\15382\Desktop\Wind\CL_ROSCO\references\ROSCO\rosco\toolbox\control_interface.py`

It exposes `ControllerInterface` for calling the compiled controller. Consult the
local ROSCO source and examples instead of recreating `avrSWAP` from memory.

Useful examples:

- `Examples\04_simple_sim.py`: controller DLL around a simple Python plant.
- `Examples\05_openfast_sim.py`: ROSCO with OpenFAST.
- `Examples\07_openfast_outputs.py`: `.dbg3`/`avrSWAP` logging.
- `Examples\14_open_loop_control.py`: prescribed controller actions.
- `Examples\17a_zeromq_simple.py`: ZeroMQ interface example.

## Workflow

1. Freeze a controller identity: DLL hash, compatible `DISCON.IN`, ROSCO source or
   release, turbine tuning file, interface version, and required auxiliary files.
   Run `scripts/check_controller_bundle.py` to verify hashes and initialize the
   pair through the official `ControllerInterface` before a scientific run.
2. Run the OpenFAST reference and log the full controller/plant exchange when
   possible.
3. Build an explicit semantic map between ROSCO interface records and learned-plant
   measurements/commands, including units, signs, timing, filtering, and limits.
4. Replay recorded commands for open-loop plant validation.
5. Instantiate a fresh ROSCO controller state for each closed-loop case and connect
   it to the identified plant through `ControllerInterface`.
6. Compare paired loops with identical wind, initialization, controller settings,
   time step, and termination rules.

Do not label ROSCO's pass-through example as an uncontrolled or controller-free
OpenFAST baseline. Specify exactly which signals and controls are passed through.

Do not identify a DLL as ROSCO from its filename, directory, exported `DISCON`
symbol, or initialization message. Require provenance plus a behavioral check that
the DLL reads and validates `DISCON.IN`. For new ROSCO experiments, use one pinned,
verified ROSCO release/library and generate turbine-specific `DISCON.IN` files
through that release's tuning workflow.
