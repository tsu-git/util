#!/usr/bin/python

def sum_data_set(input_num_str: str) -> dict:
    import re
    
    summary = 0

    if matched := re.search('[^0-9]', input_num_str):
        return({'ret':False})

    for x in input_num_str:
        summary += int(x)

    return({'ret':True, 'summary':summary})

if __name__ == "__main__":
    import sys

    prompt = "input data_set: "
    END_DATA_SET = '0'

    while True:
        data_set = input(prompt).strip()
        if data_set == END_DATA_SET:
            break

        summary = 0
        ret = sum_data_set(data_set)
        if ret["ret"] is False:
            print(f"invalid data_set [{data_set}]")
            continue
        print(ret["summary"])


    sys.exit()

