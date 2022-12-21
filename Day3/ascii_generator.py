import string


def generate_ascii_dict():
    ascii_dict = dict()
    ascii_values = [character for character in enumerate(list(
        string.ascii_lowercase + string.ascii_uppercase), 1)]
    for score, letter in ascii_values:
        ascii_dict.update({letter: score})
    return ascii_dict
