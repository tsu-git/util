#!/usr/bin/python

if __name__ == "__main__":
    import sys

    prompt_1 = "input source string: "
    prompt_2 = "input target string: "

    while True:
        try:
            s = input(prompt_1).strip()
        except EOFError:
            break

        if len(s) > 0:
            break
        
    while True:
        try:
            p = input(prompt_2).strip()
        except EOFError:
            break

        if len(p) > 0:
            break

    ring_s = s + s
    if p in ring_s:
        print("Yes")
    else:
        print("No")


    sys.exit()

