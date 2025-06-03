def read_names(path: str) -> list[tuple[str, str, str]]:
    with open(path, "r", encoding = "utf -8") as file:
        names = []
        for line in file.readlines():
            name = tuple(line.strip().split(" "))
            names.append(name)
    return names
