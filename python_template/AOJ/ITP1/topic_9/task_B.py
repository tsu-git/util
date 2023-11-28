#!/usr/bin/python


if __name__ == "__main__":
    import sys

    prompt_1 = "input string as cards: "
    prompt_2 = "input number of shuffles (m): "
    prompt_3 = "input number of a shuffle cards (h): "
    END_OF_INPUT = "-"

    cards_list = []

    while True:
        """ in order to avoid EOFError, use try-except
        """
        try:
            cards = input(prompt_1).strip()
            if cards == END_OF_INPUT:
                break
        except EOFError:
            """ This exception seems to occur only when specific 
                environment like a code competition env and like that.
            """
            break

        m = int(input(prompt_2).strip())
        
        for i in range(m):
            h = int(input(prompt_3).strip())
            cards = cards[h:] + cards[:h]
        cards_list.append(cards)


    for each_set in cards_list:
        print(each_set)

    sys.exit()

