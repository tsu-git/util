#!/usr/bin/python

def require_divisors(num: int) -> list:
    divisors = []
    for i in range(1, num+1):
        if (num % i) > 0:
            continue
        divisors.append(i)

    return(divisors)


def require_common_divisors(set_x: set, set_y: set) -> set:
    common_div = set_x & set_y

    return(common_div)


if __name__ == "__main__":
    import sys

    prompt = "input two numbers (x, y): "

    x, y = map(int, input(prompt).strip().split())

    x_set = {i for i in require_divisors(x)}
    y_set = {i for i in require_divisors(y)}

    common_div = sorted(list(require_common_divisors(x_set, y_set)))
    greate_common_div = common_div[-1]

    print(greate_common_div)

    sys.exit()

