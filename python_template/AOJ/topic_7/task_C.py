#!/usr/bin/python

if __name__ == "__main__":
    import sys

    MIN_NUM_ROW_AND_COL = 1
    MAX_NUM_ROW_AND_COL = 100
    ELEM_INIT = 0

    prompt_1 = "input two integers (r: number of row, c: number of column: "
    prompt_2 = "input row data of the table by number of column: "

    r, c = map(int, input(prompt_1).strip().split())

    if (MIN_NUM_ROW_AND_COL <= r <= MAX_NUM_ROW_AND_COL) is False:
           print(f"invalid number r[{r}]")
           sys.exit()
    elif (MIN_NUM_ROW_AND_COL <= c <= MAX_NUM_ROW_AND_COL) is False:
           print(f"invalid number r[{c}]")
           sys.exit()
        
    # initialize new table
    tbl = [[ELEM_INIT for i in range(c + 1)] for j in range(r + 1)]

    for i in range(r):
        line = list(map(int, input(prompt_2).strip().split()))
        for j in range(c + 1):
            if j < c:
                elem = line[j]
            else:
                elem = sum(tbl[i])
            tbl[i][j] = elem
            tbl[r][j] += elem # row of ground total

    for i in range(r + 1):
        for j in range(c + 1):
            if j < c:
                end_char = " "
            else:
                end_char = ""
            print(tbl[i][j], end=end_char)
        print()

    sys.exit()

