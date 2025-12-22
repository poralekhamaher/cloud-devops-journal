import logging
import sys
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "run.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def read_input(path: str) -> tuple[str, int]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        logging.error("input.txt not found")
        sys.exit(1)

    if len(lines) < 2:
        logging.error("input.txt has insufficient lines")
        sys.exit(2)

    name = lines[0]

    try:
        number = int(lines[1])
    except ValueError:
        logging.error("Number in input.txt is not an integer")
        sys.exit(3)

    return name, number


def write_output(path: str, name: str, number: int) -> None:
    results = [f"User: {name}"]

    for i in range(1, number + 1):
        if i % 2 == 0:
            results.append(str(i))

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(results) + "\n")

    logging.info("output.txt written successfully")


def main():
    logging.info("Job started")

    name, number = read_input("input.txt")
    write_output("output.txt", name, number)

    logging.info("Job completed successfully")


if __name__ == "__main__":
    main()