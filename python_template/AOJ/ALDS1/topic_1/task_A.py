#!/usr/bin/python

def print_array(in_list: list):
    for i in range(len(in_list)):
        if i < len(in_list) - 1:
            sep = " "
        else:
            sep = "\n"
        print(in_list[i], end=sep)

    return()


if __name__ == "__main__":
    import sys

    prompt_1 = "input number of array elements: "
    prompt_2 = "input integers to fill in each elements: "

    N = int(input(prompt_1).strip())
    A = list(map(int, input(prompt_2).strip().split()))

    print_array(A)

    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        print_array(A)

    sys.exit()

