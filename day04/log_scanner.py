from __future__ import annotations

import logging
from pathlib import Path
import sys


INPUT_PATH = Path("app.log")
OUTPUT_PATH = Path("output/flagged.log")
LOG_PATH = Path("logs/run.log")


def setup_logging() -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(LOG_PATH, encoding="utf-8"),
        ],
    )


def read_lines(path: Path) -> list[str]:
    # TODO: implement robust file read (UTF-8), raise FileNotFoundError if missing
    raise NotImplementedError


def filter_flagged(lines: list[str]) -> tuple[list[str], int, int]:
    """
    Return (flagged_lines, warning_count, error_count)
    Rules:
      - A line is flagged if it contains "WARNING" or "ERROR" (case-sensitive).
    """
    # TODO: implement filtering + counts
    raise NotImplementedError


def write_output(path: Path, lines: list[str]) -> None:
    # TODO: ensure output folder exists, write lines exactly (preserve original line endings where possible)
    raise NotImplementedError


def main() -> int:
    setup_logging()
    logging.info("start input=%s output=%s", INPUT_PATH, OUTPUT_PATH)

    try:
        lines = read_lines(INPUT_PATH)
    except FileNotFoundError:
        logging.error("input missing: %s", INPUT_PATH)
        return 1
    except Exception as e:
        logging.exception("unexpected read failure: %s", e)
        return 3

    try:
        flagged, warn_ct, err_ct = filter_flagged(lines)
        write_output(OUTPUT_PATH, flagged)
    except Exception as e:
        logging.exception("unexpected processing failure: %s", e)
        return 3

    total = len(flagged)
    logging.info("summary warning=%d error=%d total_flagged=%d", warn_ct, err_ct, total)

    if total == 0:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
