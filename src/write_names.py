def write_names(names: list[str], path: str) -> None:
    with open(path, "w", encoding="utf-8") as file:
        for name in names:
            file.write(name + "\n")
