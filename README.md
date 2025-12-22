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