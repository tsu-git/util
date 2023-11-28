#!/usr/bin/python

if __name__ == "__main__":
    import sys

    prompt_1 = "input number of cards (n): "
    prompt_2 = "input animal name of two cards: "

    num_cards = int(input(prompt_1).strip())
    score_taro = 0
    score_hanako = 0

    for i in range(num_cards):
        card_taro, card_hanako  = input(prompt_2).strip().split()
        if card_taro > card_hanako:
            score_taro += 3
        elif card_taro < card_hanako:
            score_hanako += 3
        else:
            score_taro += 1
            score_hanako += 1

    print(score_taro, score_hanako)

    sys.exit()

