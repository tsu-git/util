#!/usr/bin/python


if __name__ == "__main__":
    import sys
    
    prompt_1 = "input two integer as n(row) and m(column): "
    prompt_2 = "input table data by n rows and m columns: "
    prompt_3 = "input single column data by m rows: "

    n, m = map(int, input(prompt_1).strip().split())

    tbl = []
    for i in range(n + m):
        if i < n:
            tbl.append(list(map(int, input(prompt_2).strip().split())))
        else:
            tbl.append(int(input(prompt_3).strip()))


    A = tbl[:n]
    b = tbl[n:]

    for i in range(n):
        c = 0
        for j in range(m):
            c += A[i][j] * b[j]
        print(c)

    sys.exit()
