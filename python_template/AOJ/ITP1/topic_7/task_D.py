#!/usr/bin/python

if __name__ == "__main__":
    import sys

    MIN_NUM_OF_ELEM = 1
    MAX_NUM_OF_ELEM = 100

    prompt_1 = "input integers (n, m, l): "
    prompt_2 = "input A data(n by m), then B data(m by l): "

    n, m, l = map(int, input().strip().split())

    A = [[0 for i in range(m)] for j in range(n)]
    B = [[0 for i in range(l)] for j in range(m)]
    C = [[0 for i in range(l)] for j in range(n)]

    for i in range(n + m):
        line = list(map(int, input().strip().split()))
        if i < n:
            if len(line) != m:
                print("invalid number of elements for A")
                sys.exit()
            else:
                A[i] = line
        else:
            if len(line) != l:
                print("invalid number of elements for B")
                sys.exit()
            else:
                B[i - n] = line

    for i in range(n):
        for j in range(l):
            for k in range(m):
                x, y = A[i][k], B[k][j]
                C[i][j] += x * y

    for i in range(len(C)):
        for j in range(len(C[i])):
            if j < len(C[i]) - 1:
                end_char = " "
            else:
                end_char = ""

            print(C[i][j], end=end_char)
        print()


    sys.exit()

