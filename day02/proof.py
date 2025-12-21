def read_input(path: str) -> tuple[str, int]:
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]

    if len(lines) < 2:
        raise ValueError("input.txt must contain 2 lines: name then number")

    name = lines[0]
    number = int(lines[1])  # raises ValueError if invalid
    return name, number


def write_output(path: str, name: str, number: int) -> None:
    results = [f"User: {name}"]

    for i in range(1, number + 1):
        if i % 2 == 0:
            results.append(str(i))

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(results) + "\n")


def main():
    try:
        name, number = read_input("input.txt")
    except FileNotFoundError:
        print("Missing input.txt")
        return
    except ValueError:
        print("Invalid input file")
        return

    write_output("output.txt", name, number)
    print("Processed input.txt → output.txt")


if __name__ == "__main__":
    main()
