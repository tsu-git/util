#!/usr/bin/python

def print_str(input_str: str, start: int, end: int) -> str:
    if 0 <= start <= end <= len(input_str) is False:
        return(None)
    
    output_str = input_str[start:end+1]
    print(output_str)

    return(output_str)


def reverse_str(input_str: str, start: int, end: int) -> str:
    if 0 <= start <= end <= len(input_str) is False:
        return(None)

    output_str = input_str[:start]
    for c in reversed(input_str[start:end+1]):
        output_str += c
    output_str += input_str[end+1:]

    return(output_str)


def replace_str(input_str: str, start: int, end: int, rep: str) -> str:
    if 0 <= start <= end <= len(input_str) is False:
        return(None)
    elif (end - start + 1) == len(input_str) is False:
        return(None)

    return(input_str[:start] + rep + input_str[end+1:])


if __name__ == "__main__":
    import sys

    prompt_1 = "input string: "
    prompt_2 = "input number of comands: "
    prompt_3 = "input command with arguments: "

    INDX_COMMAND = 0
    INDX_START   = 1
    INDX_END     = 2
    INDX_REPLACE = 3

    MIN_ELEM_OF_COMMAND_LINE = 3

    received_str = input(prompt_1).strip()
    q = int(input(prompt_2).strip())

    i = 0
    while True:
        if i >= q:
            break

        command_line = list(input(prompt_3).strip().split())
        if len(command_line) < MIN_ELEM_OF_COMMAND_LINE:
            print(f"invalid number of element in command [{command_line}]")
            continue

        a = int(command_line[INDX_START])
        b = int(command_line[INDX_END])

        if command_line[INDX_COMMAND] == "print":
            ret = print_str(received_str, a, b)
            if ret is None:
                print(f"invalid arguments: f{command_line}")
        elif command_line[INDX_COMMAND] == "reverse":
            ret = reverse_str(received_str, a, b)
            if ret is None:
                print(f"invalid arguments: f{command_line}")
            received_str = ret
        elif command_line[INDX_COMMAND] == "replace":
            ret = replace_str(
                received_str, a, b, command_line[INDX_REPLACE])
            if ret is None:
                print(f"invalid arguments: f{command_line}")
            received_str = ret
        else:
            print(f"invalid command [{command_line}]")
            continue

        i += 1


    sys.exit()

