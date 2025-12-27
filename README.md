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
`day04/log_scanner.py`,`day04/app.log`,`day04/output/flagged.log`,`day04/logs/run.log`

## Day 5 — Server Health Check Script (Disk/CPU/Memory Logging)
- Built a non-interactive health check script for ops monitoring
- Captures key system signals:
  - Disk usage percentage (via `shutil.disk_usage`)
  - CPU usage percentage (via `psutil.cpu_percent`)
  - Memory usage percentage (via `psutil.virtual_memory`)
- Writes timestamped operational logs to `logs/health.log` using Python `logging`
- Designed for unattended execution (cron/Task Scheduler friendly)
- Exit codes:
  - `0` = success (metrics recorded)
  - `1` = missing dependency (`psutil` not installed)
  - `3` = unexpected failure (exception logged)

**Artifact**:
`day05/server_health.py`,`day05/logs/health.log`

## Day 6-7 — Refactoring to Professional CLI Tool (ops_tool.py)

### Day 6: Argument Parsing + Logging + Modular Functions
- Replaced `input()` with `argparse` for non-interactive CLI execution
- Added `--name` and `--number` command-line arguments
- Replaced `print()` with `logging` module for ops-ready output
- Split monolithic code into testable functions:
  - `parse_args()` for argument handling
  - `generate_evens(number)` for business logic
  - `write_output(name, evens)` for file I/O
- Maintained proper exit codes (0=success, 1=failure)
- Understanding why CLI tools use argparse in cron/CI/CD contexts

**Artifact**: `day06_07_refactor/ops_tool.py` (evens mode only)

### Day 7: Multi-Mode Operations Tool (Unified Script)
- Extended ops_tool.py with `--mode` argument for multiple operations:
  - `--mode evens` → even number generator (Day 1-3 logic)
  - `--mode scan` → log file scanner for ERROR/WARNING (Day 4 logic)
  - `--mode health` → system health metrics collection (Day 5 logic)
- Single unified tool with shared logging infrastructure
- Consistent exit code strategy across all modes
- Demonstrated code reusability and professional script design

**Artifact**: `day06_07_refactor/ops_tool.py` (complete), `output.txt`, `logs/run.log`

## BREAK NOTICE

**Day 8 begins January 1, 2025.**

Until then: re-practicing Day 1-7 code, reinforcing fundamentals, and preparing for Linux + Git deep-dive.
Today (27/12/2025) was taken as a rest day. No study or coding tasks were performed.
Time was spent on system setup and recreation (installed Knulli OS on a retro console and ported games).
Regular study schedule resumes next session.