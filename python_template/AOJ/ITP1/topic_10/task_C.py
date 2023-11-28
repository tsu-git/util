#!/usr/bin/python

if __name__ == "__main__":
    import sys
    import statistics

    prompt_1 = "input number of students: "
    prompt_2 = "input scores of the each students: "
    END_OF_INPUT = 0

    while True:
        n = int(input(prompt_1).strip())
        if n == END_OF_INPUT:
            break

        scores = list(map(int, input(prompt_2).strip().split()))
        if len(scores) != n:
            print("invalid number of scores. "
                f"expected[{n}] received[{len(scores)}]")
        avg = sum(scores) / len(scores)
        print("{0:.5f}".format(statistics.pstdev(scores, avg)))


    sys.exit()
