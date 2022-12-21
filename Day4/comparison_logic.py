from file_formatting import clean_gen


def sections_list(file_path: str) -> list:
	return [section for section in clean_gen(file_path)]


def create_range_set(range_list: list) -> set:
	return set([r for r in range(int(range_list[0]), int(range_list[1]) + 1)])


def create_duplicate_set(range1: list, range2: list) -> set:
	return create_range_set(range1) & create_range_set(range2)


def contains_in_set(range1: list, range2: list) -> int:
	for items in create_range_set(range1):
		if items in create_range_set(range2):
			return 1
	return 0


def range_creation(sections):
	ranges = [section.split("-") for section in sections.split(",")]
	return [r for r in ranges[0]], [r for r in ranges[1]]


def contains_in_comparison_counter(file_path: str) -> int:
	counter = 0
	for sections in sections_list(file_path):
		range1, range2 = range_creation(sections)
		counter += contains_in_set(range1, range2)
	return counter


def duplicate_comparison_counter(file_path: str) -> int:
	counter = 0
	for sections in sections_list(file_path):
		range1, range2 = range_creation(sections)
		comp = create_duplicate_set(range1, range2)
		range1 = create_range_set(range1)
		range2 = create_range_set(range2)
		if comp == range1 or comp == range2:
			counter += 1

	return counter
