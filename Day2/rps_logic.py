from elf_configurations import (
    cypher,
    combinations,
    map1,
    map2,
    scores,
    points_table
)


def player2_mapping(choice1: str, choice2: str):
    player2 = map1.get(combinations.get(cypher.get(choice2)).get(choice1))
    player2_hand = combinations.get(cypher.get(choice2)).get(choice1)
    return player2, player2_hand


def winner_logic(player1: int, player2: int, choice2: str):
    winner = points_table[player1][player2]
    if winner == player1:
        return scores.get("L") + scores.get(choice2)
    elif winner == player2:
        return scores.get("W") + scores.get(choice2)
    else:
        return scores.get("D") + scores.get(choice2)


def rps_score1(choice1: str, choice2: str):
    player1 = map1.get(choice1)
    player2 = map2.get(choice2)
    return winner_logic(player1, player2, choice2)


def rps_score2(choice1: str, choice2: str):
    player1 = map1.get(choice1)
    player2, player2_hand = player2_mapping(choice1, choice2)
    return winner_logic(player1, player2, choice2)


def round_score(strategy_choice: list, part: int):
    player1 = str(strategy_choice[0])
    player2 = str(strategy_choice[1])
    if part == 1:
        return rps_score1(player1, player2)
    if part == 2:
        return rps_score2(player1, player2)
