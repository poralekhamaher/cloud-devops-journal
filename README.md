# cloud-devops-journal
Daily execution log for Python, Linux, and automation fundamentals with strict Git discipline.

## Day 1 — Python Fundamentals + File Output
- Using `input()` and type conversion with try/except
- For-loops, `range()`, and modulo filtering
- Writing output to files with `open()`
- Running scripts from terminal and verifying output
- Git: add, commit, push workflow

**Artifact**: `day01/proof.py`, `day01/output.txt`

## Day 2 — File-Based Automation (Non-Interactive)
- Removed `input()` calls for non-interactive execution
- Reading structured data from files (`input.txt`)
- Separating logic into functions for reusability
- Handling errors gracefully (missing/invalid files)
- Writing deterministic automation scripts

**Artifact**: `day02/proof.py`, `day02/input.txt`, `day02/output.txt`

## Day 3 — Logging + Exit Codes (Ops-Ready Scripts)
- Replaced `print()` with Python's `logging` module
- Writing timestamped logs to `logs/run.log`
- Using exit codes (0=success, 1/2/3=different failures) for monitoring
- Making scripts machine-detectable for cron/CI/CD systems
- Understanding log levels (INFO, ERROR) and format strings
- Testing failure modes deliberately (missing file, invalid data)

**Artifact**: `day03/proof.py`, `day03/input.txt`, `day03/output.txt`, `day03/logs/run.log`

## Day 4 — Log Scanning Automation (Error & Warning Detection)
- Built a non-interactive log scanning script for ops-style automation
- Reading application logs from a fixed file path (`app.log`)
- Filtering and extracting only `ERROR` and `WARNING` log entries
- Writing flagged log lines to a dedicated `output/` directory
- Creating operational logs in `logs/run.log` using Python `logging`
- Implemented clear exit codes for automation and monitoring:
  - `0` = success, flagged entries found
  - `1` = input log file missing
  - `2` = no errors or warnings found
  - `3` = unexpected failure
- Used relative paths to avoid duplicated directories when running scripts
- Enforced job-style folder isolation (code vs output vs logs)
- Practiced failure testing by deliberately breaking inputs

**Artifact**:
`day04/log_scanner.py`,
`day04/app.log`,
`day04/output/flagged.log`,
`day04/logs/run.log`
