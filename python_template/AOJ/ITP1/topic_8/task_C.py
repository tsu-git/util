#!/usr/bin/python


if __name__ == "__main__":
    import sys

    prompt = "input string: "
    MAX_LEN = 1200
    NUM_ALPHA = ord('z') - (ord('a') - 1)
    NUM_CHAR_NONE = 0

    counter = [NUM_CHAR_NONE for i in range(NUM_ALPHA)]

    while True:
        try: 
            line = input(prompt).strip()
        except EOFError:
            break

        if len(line) >= MAX_LEN:
            print(f"length over [{len(line)}]")
            print(f"needs within {len(line)}")
            continue

        for c in line:
            if c.isalpha() is False:
                continue
            if c.isupper():
                c = c.lower()
            i = ord(c) - ord('a')
            counter[i] += 1

            
    for i in range(NUM_ALPHA):
        charactor = chr(ord('a') + i)
        print(f"{charactor} : {counter[i]}")


    sys.exit()

