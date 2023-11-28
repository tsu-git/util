#!/usr/bin/python

""" This program is slow to pass the limit of the time needed for 
    the problem. Because the in_combination function search the input array
    linearly.
    """

def in_combination(combination_list: list, in_comb: set) -> bool:
    SAME_COMB = 0

    if len(combination_list) < 1:
        return(False)

    match = False
    for comb in combination_list:
        if len(comb ^ in_comb) != SAME_COMB: 
            continue
        else:
            match = True

    if match:
        return(match)
    else:
        return(False)


if __name__ == "__main__":
    import sys

    prompt = ("input two integers (n: max number, "
              "x: number of the summary): ")
    END_FLG = 0
    MIN_NUM = 3
    MAX_NUM = 100
    MIN_SUM = 0
    MAX_SUM = 300

    while True:
        n, x = map(int, input(prompt).strip().split())
        if n == END_FLG and x == END_FLG:
            break
        if (MIN_NUM <= n <= MAX_NUM) is not True:
            print(f"invalid n[{n}]")
            continue
        elif (MIN_SUM <= x <= MAX_SUM) is not True:
            print(f"invalid x[{x}]")
            continue

        combination_list = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                for k in range(1, n+1):
                    if i == j or j == k or k == i:
                        continue
                    elif i + j + k != x:
                        continue
                    else:
                        combi = {i, j, k}
                        if in_combination(combination_list, combi):
                            continue
                        else:
                            combination_list.append(combi)

        print(len(combination_list))


    sys.exit()
