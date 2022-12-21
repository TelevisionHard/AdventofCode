def strategy_list_gen(file_path: str):
	with open(file_path, "r") as strategy:
		text_content = strategy.read().split("\n\n")
		return [line.splitlines() for line in text_content]


def strategy_choices(file_path: str):
	for choice in strategy_list_gen(file_path):
		return [this.split() for this in choice]
