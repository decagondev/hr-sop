"""Shared runtime helpers for SOP step runners."""
import subprocess
import sys

def log(msg):
    print(f"  · {msg}", flush=True)

def run_cmd(cmd, check=True):
    log(f"$ {cmd}")
    r = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if r.stdout.strip():
        log(r.stdout.strip())
    if r.returncode != 0:
        log(f"[exit {r.returncode}] {r.stderr.strip()}")
        if check:
            raise RuntimeError(f"command failed: {cmd}")
    return r

def confirm(prompt):
    if not sys.stdin.isatty():
        raise RuntimeError(f"confirmation required but no TTY: {prompt}")
    ans = input(f"  ?? {prompt} [y/N]: ").strip().lower()
    if ans not in {"y", "yes"}:
        raise SystemExit("aborted by operator")
