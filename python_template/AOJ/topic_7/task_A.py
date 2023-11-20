#!/usr/bin/python

GRADE_FAIL = -1
GRADE_A = 80
GRADE_B = 65
GRADE_C = 50
GRADE_D = 30

def grade(m: int = -1, f: int = -1, r: int = -1) -> int:

    if m == GRADE_FAIL or f == GRADE_FAIL:
        gr = 'F'
    elif m + f >= GRADE_A:
        gr = 'A'
    elif m + f >= GRADE_B:
        gr = 'B'
    elif m + f >= GRADE_C or r >= GRADE_C:
        gr = 'C'
    elif m + f >= GRADE_D:
        gr = 'D'
    else:
        gr = 'F'


    return(gr)

if __name__ == "__main__":
    import sys

    prompt = "input scores(midterm, final, retest): "
    NUM_STUDENTS = 50
    
    grades = []
    for i in range(50):
        m, f, r = list(map(int, input(prompt).strip().split()))
        if m == GRADE_FAIL and f == GRADE_FAIL and r == GRADE_FAIL:
            break

        grades.append(grade(m, f, r))


    for grade in grades:
        print(grade)


    sys.exit()
