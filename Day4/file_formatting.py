def clean_list_gen(file_path: str) -> list:
    with open(file_path, "r") as clean_file:
        text_content = clean_file.read().split("\n\n")
        return [line.splitlines() for line in text_content]


def clean_gen(file_path: str) -> list:
    for clean in clean_list_gen(file_path):
        return [this.split()[0] for this in clean]