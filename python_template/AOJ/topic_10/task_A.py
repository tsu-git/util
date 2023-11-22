#!/usr/bin/python

if __name__ == "__main__":
    import sys
    import math

    prompt = "input two points as coordinate (x1, y1, x2, y2): "

    x1, y1, x2, y2 = map(float, input(prompt).strip().split())
    length_x = x2 - x1
    length_y = y2 - y1

    length_p1_p2 = math.sqrt(length_x ** 2 + length_y ** 2)  
    print(f"{length_p1_p2:.5f}")

    sys.exit()

