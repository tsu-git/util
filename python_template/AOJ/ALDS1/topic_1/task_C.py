#!/usr/bin/python
import math

def isprime(x: int) -> bool:
    if x == 2:
        return(True)

    if x < 2 or x % 2 == 0:
        return(False)

    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return(False)
        i += 2

    return(True)


if __name__ == "__main__":
    import sys

    prompt_1 = "input a number of lines: "
    prompt_2 = "input a integer: "

    n = int(input(prompt_1).strip())
    num_of_prime = 0

    i = 0
    while True:
        if i >= n:
            break

        try:
            num = int(input(prompt_2).strip())
        except ValueError:
            print(f"received invalid data [{num}]")

        if isprime(num):
            num_of_prime += 1

        i += 1

    print(num_of_prime)

    sys.exit()

