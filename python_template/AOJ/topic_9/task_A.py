#!/usr/bin/python

if __name__ == "__main__":
    import sys

    prompt_1 = "input search_word: "
    prompt_2 = "input article: "
    
    while True:
        try:
            W = input(prompt_1).strip()
        except EOFError:
            break

        if len(W) > 0:
            break
    
    W = W.lower()

    article = {}
    while True:
        try:
            for word in list(input(prompt_2).strip().split()):
                if word == "END_OF_TEXT":
                    article[word] = 1
                    break
                word = word.lower()
                if word in article:
                    article[word] += 1
                else:
                    article[word] = 1
        except EOFError:
            break

        if "END_OF_TEXT" in article:
            break


    print(f"{article[W]}")

    sys.exit()

