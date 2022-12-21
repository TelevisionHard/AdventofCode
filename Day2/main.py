from file_formatting import strategy_choices
from rps_logic import (
	round_score
)


def main(data: str, part: int):
    return sum(
	    [round_score(choice, part) for choice in strategy_choices(data)]
    )


if __name__ == "__main__":
    print(main("data/data.txt", 2))
