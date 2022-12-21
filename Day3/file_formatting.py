def bag_list_gen(file_path: str):
    with open(file_path, "r") as bag_file:
        text_content = bag_file.read().split("\n\n")
        return [line.splitlines() for line in text_content]


def bag_gen(file_path: str):
    for bags in bag_list_gen(file_path):
        return [this.split()[0] for this in bags]
