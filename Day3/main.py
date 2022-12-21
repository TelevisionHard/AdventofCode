from bag_logic import (
	score_gen,
	score_gen2
)


def main(file_path: str, part: int):
	if part == 1:
		return score_gen(file_path)
	if part == 2:
		return score_gen2(file_path)
	else:
		raise ValueError("Please use integer within range 1-2")


if __name__ == "__main__":
	print(main("data/bags.txt", 2))
