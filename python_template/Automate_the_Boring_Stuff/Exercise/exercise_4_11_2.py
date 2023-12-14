#!/usr/bin/python

import random
import unittest

class Test_exercise_4_11_2(unittest.TestCase):
    def test_roll_the_dice(self):
        self.assertTrue(type(roll_dice()) == list)
        for i in roll_dice():
            self.assertTrue(type(i) == int)
            self.assertTrue(i == 0 or i == 1)

    def test_roll_the_dice(self):
        out_streak = []
        self.assertTrue(
            type(search_streak_of_same_sides(out_streak)) == bool)
        self.assertTrue(
            type(search_streak_of_same_sides(out_streak)) == bool)

        out_streak = [1 for i in range(6)]
        out_streak.append(1)
        self.assertTrue(search_streak_of_same_sides(out_streak))

        out_streak = [0 for i in range(6)]
        out_streak.append(1)
        self.assertTrue(search_streak_of_same_sides(out_streak))

        out_streak.insert(0, 1)
        out_streak.append(0)
        self.assertFalse(search_streak_of_same_sides(out_streak))

        out_streak.insert(2, 1)
        out_streak.append(0)
        self.assertFalse(search_streak_of_same_sides(out_streak))

        out_streak[-1] = 1
        out_streak.append(0)
        self.assertFalse(search_streak_of_same_sides(out_streak))


def roll_dice() -> list:
    streak = []
    summary = 0
    num_of_roll = 6

    for i in range(num_of_roll):
        side = random.randint(0, 1)
        streak.append(side)
        summary += side

    if summary == 0 or summary == num_of_roll:
        streak.append(1)

    return(streak)


def search_streak_of_same_sides(in_streak: list) -> bool:
    if len(in_streak) < 1:
        return(False)

    if in_streak[-1] == 1:
        return(True)
    else:
        return(False)
        

if __name__ == "__main__":
    import sys

    #unittest.main()
    
    EXPERIMENT_NUM = 10000
    number_of_streaks = 0

    # try to make list 10,000
    for i in range(EXPERIMENT_NUM):
        # roll the dice and make list
        streak_of_num = roll_dice()
        # search a streak of same sides
        if (search_streak_of_same_sides(streak_of_num)):
            number_of_streaks += 1


    print(('Probability of apparrencing the same side: '
        f'{(number_of_streaks / EXPERIMENT_NUM) * 100}%'))

    sys.exit()
