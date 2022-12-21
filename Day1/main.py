from file_formatter import file_formatter
from data_builder import (
	max_elf_calories,
	total_elf_calories
)


def main(file_path: str, part: int):
	calories = file_formatter(file_path)
	if part == 1:
		return max_elf_calories(calories)
	if part == 2:
		return total_elf_calories(calories)
	else:
		raise ValueError("Not in int range: 1-2")


if __name__ == "__main__":
	print(main("data/calories.txt", 2))
