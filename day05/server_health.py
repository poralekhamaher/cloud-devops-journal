from __future__ import annotations

import logging
from pathlib import Path
from datetime import datetime
import shutil
import sys

import psutil  # pip install psutil


LOG_PATH = Path("logs/health.log")


def setup_logging() -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.FileHandler(LOG_PATH, encoding="utf-8")],
    )


def get_disk_percent(path: str = ".") -> float:
    # TODO: use shutil.disk_usage and return used percentage (0-100)
    raise NotImplementedError


def get_cpu_percent() -> float:
    # TODO: use psutil.cpu_percent with a short sample interval (e.g., 0.2)
    raise NotImplementedError


def get_mem_percent() -> float:
    # TODO: use psutil.virtual_memory().percent
    raise NotImplementedError


def main() -> int:
    setup_logging()

    try:
        disk = get_disk_percent(".")
        cpu = get_cpu_percent()
        mem = get_mem_percent()

        logging.info("health disk=%.1f%% cpu=%.1f%% mem=%.1f%%", disk, cpu, mem)

        # TODO: optional thresholds for warning (example):
        # if disk >= 90 or cpu >= 90 or mem >= 90: return 2
        return 0

    except ModuleNotFoundError:
        logging.error("psutil not installed. Run: pip install psutil")
        return 1
    except Exception as e:
        logging.exception("unexpected failure: %s", e)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())