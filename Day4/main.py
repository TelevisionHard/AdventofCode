from comparison_logic import (
	duplicate_comparison_counter,
	contains_in_comparison_counter
)


def main(file_path: str, part: int) -> int:
	if part == 1:
		return duplicate_comparison_counter(file_path)
	if part == 2:
		return contains_in_comparison_counter(file_path)
	else:
		raise ValueError("Please use integer within range 1-2")


if __name__ == "__main__":
	print(main("data/data.txt", 2))
