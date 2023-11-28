#!/usr/bin/python

def translate_case(input_line: str) -> str:
    
    output_line = ""

    for c in input_line:
        if c.isupper():
            output_line += c.lower()
        elif c.islower:
            output_line += c.upper()
        else:
            output_line += c

    return(output_line)


if __name__ == "__main__":
    import sys

    prompt = "input string: "

    MAX_LEN = 1200

    line = ""

    """ in order to avoid EOFError, use try-except
    """
    try:
        while True:
            line = input(prompt).strip()
            if len(line) >= MAX_LEN:
                print(f"String length needs to be below {MAX_LEN}")
                break
            translated_line = translate_case(line)
            print(translated_line)

    except EOFError:
        pass
        # This exception will occur only when the competition environment


    sys.exit()

