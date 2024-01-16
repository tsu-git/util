import sys, random, re, time
from datetime import datetime

def show_question(min: int, max: int) -> int:
    N = random.randint(min, max)
    M = random.randint(min, max)
    print(f"Q: {N} * {M} = ?")
    return N * M

MIN_NUM = 0
MAX_NUM = 9
NUM_OF_QUESTION = 2

# provide questions 10 times
for i in range(NUM_OF_QUESTION):
    # show a question
    correct_ans = show_question(MIN_NUM, MAX_NUM)

    # get start time
    start_tm = datetime.now()

    # let user input the answer
    prompt = "  input your answer: "
    try_cnt = 0
    while True:
        if try_cnt >= 3:
            print(f"  Retry over!")
            break

        ans = input(prompt).strip()
        if match := re.search('^\d+$', ans):
            ans = int(ans)
            try_cnt += 1
        else:
            print(f"  received invalid value: {ans}")
            continue

        # determine this is failed, if it's 8 minuites over
        #   get current time
        current_tm = datetime.now()
        #   calculate the elapsed time
        elapsed_tm = current_tm - start_tm
        if elapsed_tm.seconds > 8:
            print(f"  Time over!")
            break
            
        # verify the answer
        if ans == correct_ans:
            # show "Correct!", if the answer is right
            print(f"  Correct! [{ans}]")
            break
        else:
            print(f"  Failed! [{ans}]")
            continue

sys.exit()
