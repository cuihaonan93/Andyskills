import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def first_match(path: Path, pattern: str) -> str | None:
    if not path.exists():
        return None
    match = re.search(
        pattern, path.read_text(encoding="utf-8", errors="replace"), re.MULTILINE
    )
    return match.group(1) if match else None


def probe_controller(rosco_root: Path, dll: Path, discon_in: Path, dt: float) -> dict:
    command = [
        sys.executable,
        str(Path(__file__).resolve()),
        "--_probe",
        "--rosco-root",
        str(rosco_root),
        "--dll",
        str(dll),
        "--discon-in",
        str(discon_in),
        "--dt",
        str(dt),
    ]
    completed = subprocess.run(command, capture_output=True, text=True, timeout=30)
    for line in reversed(completed.stdout.splitlines()):
        if line.startswith("CONTROLLER_PROBE_JSON="):
            result = json.loads(line.partition("=")[2])
            result["process_exit_code"] = completed.returncode
            return result
    return {
        "initialized": False,
        "process_exit_code": completed.returncode,
        "probe_error": (completed.stderr or completed.stdout).strip(),
    }


def run_probe(args: argparse.Namespace) -> int:
    sys.path.insert(0, str(args.rosco_root.resolve()))
    from rosco.toolbox.control_interface import ControllerInterface

    try:
        controller = ControllerInterface(
            str(args.dll.resolve()),
            param_filename=str(args.discon_in.resolve()),
            DT=args.dt,
            sim_name="controller_bundle_probe",
        )
        result = {
            "initialized": int(controller.aviFAIL.value) >= 0,
            "aviFAIL": int(controller.aviFAIL.value),
            "message": controller.avcMSG.value.decode("utf-8", "replace"),
        }
    except Exception as exc:
        result = {
            "initialized": False,
            "error": f"{type(exc).__name__}: {exc}",
        }
    print("CONTROLLER_PROBE_JSON=" + json.dumps(result, ensure_ascii=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the provenance and configuration behavior of a ROSCO bundle."
    )
    parser.add_argument("--rosco-root", required=True, type=Path)
    parser.add_argument("--dll", required=True, type=Path)
    parser.add_argument("--discon-in", required=True, type=Path)
    parser.add_argument("--dt", type=float, default=0.00625)
    parser.add_argument("--expected-dll-sha256")
    parser.add_argument("--_probe", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()

    if args._probe:
        return run_probe(args)

    for path in (args.rosco_root, args.dll, args.discon_in):
        if not path.exists():
            parser.error(f"path does not exist: {path}")

    dll_hash = sha256(args.dll)
    package_version = first_match(
        args.rosco_root / "pyproject.toml", r'^version\s*=\s*"([^"]+)"'
    )
    controller_source_version = first_match(
        args.rosco_root / "rosco" / "controller" / "src" / "ROSCO_Types.f90",
        r"rosco_version\s*=\s*'([^']+)'",
    )
    discon_generated_version = first_match(
        args.discon_in, r"written using ROSCO version\s+([^\s]+)"
    )

    valid_probe = probe_controller(args.rosco_root, args.dll, args.discon_in, args.dt)
    missing_input = args.discon_in.parent / "__rosco_bundle_probe_missing__.IN"
    if missing_input.exists():
        parser.error(f"reserved probe path already exists: {missing_input}")
    missing_probe = probe_controller(args.rosco_root, args.dll, missing_input, args.dt)

    input_source_version_match = (
        controller_source_version == discon_generated_version
        if controller_source_version and discon_generated_version
        else None
    )
    expected_hash_match = (
        dll_hash == args.expected_dll_sha256.upper()
        if args.expected_dll_sha256
        else None
    )
    reads_configuration = not missing_probe.get("initialized", False)
    approved = (
        valid_probe.get("initialized", False)
        and reads_configuration
        and input_source_version_match is not False
        and expected_hash_match is not False
    )

    warnings = []
    if package_version != controller_source_version:
        warnings.append(
            "Python package metadata and generated controller source versions differ."
        )
    if not reads_configuration:
        warnings.append(
            "DLL accepted a missing DISCON.IN and does not satisfy the ROSCO configuration contract."
        )
    if args.expected_dll_sha256 is None:
        warnings.append(
            "No expected DLL hash was supplied; record release/build provenance separately."
        )

    result = {
        "approved_for_rosco_experiment": approved,
        "rosco_root": str(args.rosco_root.resolve()),
        "python_package_version": package_version,
        "controller_source_version": controller_source_version,
        "dll": str(args.dll.resolve()),
        "dll_sha256": dll_hash,
        "expected_dll_sha256_match": expected_hash_match,
        "discon_in": str(args.discon_in.resolve()),
        "discon_in_sha256": sha256(args.discon_in),
        "discon_generated_version": discon_generated_version,
        "input_source_version_match": input_source_version_match,
        "valid_input_probe": valid_probe,
        "missing_input_probe": missing_probe,
        "reads_and_validates_discon_in": reads_configuration,
        "dt": args.dt,
        "warnings": warnings,
    }
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0 if approved else 1


if __name__ == "__main__":
    raise SystemExit(main())
