# cloud-devops-journal

Daily execution log for learning Python, Linux, and automation fundamentals
with strict Git discipline.

## Day 1 — Python Fundamentals + File Output

Learned and practiced:
- Using `input()` to accept user data
- Understanding that `input()` returns strings
- Converting strings to integers safely with try/except
- Using for-loops and `range()` correctly
- Filtering even numbers using modulo (%)
- Writing output to a file using with `open()`
- Understanding why with `open()` safely handles file closing
- Running Python scripts from the terminal
- Verifying program output via output.txt
- Committing and pushing code to GitHub

Artifact:
- day01/proof.py
- day01/output.txt

## Day 2 — File-Based Automation (Non-Interactive)

Learned and practiced:
- Removing all `input()` calls to make scripts fully non-interactive
- Reading structured data from a file (`input.txt`)
- Treating files as job/config inputs instead of human input
- Validating file contents before processing
- Separating logic into functions for readability and reuse
- Handling runtime errors gracefully (missing file, invalid data)
- Writing deterministic automation scripts that run without prompts
- Verifying results via generated output files
- Preserving Day 1 as a frozen reference point
- Using Git to track progression between script versions

Artifact:
- `day02/proof.py`
- `day02/input.txt`
- `day02/output.txt`
