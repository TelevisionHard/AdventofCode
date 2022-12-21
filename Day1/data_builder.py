
def total_calories_per_elf(elf_list: list) -> list:
	calories_per_elf = [map(int, line.splitlines()) for line in elf_list]
	return [sum(elf) for elf in calories_per_elf]


def max_elf_calories(elf_list: list) -> int:
	return max(total_calories_per_elf(elf_list))


def total_elf_calories(elf_list: list) -> int:
	return sum(sorted(total_calories_per_elf(elf_list), reverse=True)[0:3])

