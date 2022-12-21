import itertools as it
from file_formatting import bag_gen
from ascii_generator import generate_ascii_dict


def bag_grouping(file_path: str):
    return list(it.zip_longest(*[iter(bag_gen(file_path))] * 3))


def bag_split(bag_contents: str):
    bag_size = len(bag_contents)
    pocket1 = bag_contents[: int(bag_size / 2)].strip()
    pocket2 = bag_contents[int(bag_size / 2):].strip()
    return [pocket1, pocket2]


def duplicate_item_finder(pockets: list):
    pocket1 = pockets[0:1].pop()
    pocket2 = pockets[1:].pop()
    return [item for item in pocket1 if item in pocket2][0]


def group_list(file_path):
    return [group for group in bag_grouping(file_path)]


def duplicate_letter(bag_group):
    for letter in list(set(bag_group[0])):
        if letter in set(bag_group[1]) and letter in set(bag_group[2]):
            return letter


def duplicate_group_item_finder(file_path: str):
    return [duplicate_letter(group) for group in group_list(file_path)]


def score_gen(file_path: str):
    return sum([generate_ascii_dict().get(
        duplicate_item_finder(
            bag_split(str(bag)))) for bag in bag_gen(file_path)])


def score_gen2(file_path: str):
    return sum([generate_ascii_dict().get(
        letter) for letter in duplicate_group_item_finder(file_path)])
