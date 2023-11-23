#!/usr/bin/python

if __name__ == "__main__":
    import sys

    prompt_1 = "input integer: "
    prompt_2 = "input elements of vector x: "
    prompt_3 = "input elements of vector y: "

    x = int(input(prompt_1).strip())
    vector_x = list(map(int, input(prompt_2).strip().split()))
    vector_y = list(map(int, input(prompt_3).strip().split()))

    for p in range(1, 4):
        print("{0:.6f}".format(
            sum([abs(a - b) ** p for a, b in zip(vector_x, vector_y)]) ** 
            (1 / p)))

    # p is infinity
    print("{0:.6f}".format(
        max([abs(a - b) for a, b in zip(vector_x, vector_y)])))


    sys.exit()
