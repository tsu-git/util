#!/usr/bin/python

if __name__ == "__main__":
    import sys
    import numpy
    from scipy.spatial.distance import chebyshev, minkowski

    prompt_1 = "input integer: "
    prompt_2 = "input elements of vector x: "
    prompt_3 = "input elements of vector y: "

    x = int(input(prompt_1).strip())
    vector_x = list(map(int, input(prompt_2).strip().split()))
    vector_y = list(map(int, input(prompt_3).strip().split()))

    a = numpy.array(vector_x)
    b = numpy.array(vector_y)

    print("{0:.6f}".format(minkowski(a, b, 1)))
    print("{0:.6f}".format(minkowski(a, b, 2)))
    print("{0:.6f}".format(minkowski(a, b, 3)))
    print("{0:.6f}".format(chebyshev(a, b)))

    sys.exit()
