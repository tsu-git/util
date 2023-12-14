#!/usr/bin/python
import unittest

class Test_exercise_4_11_1(unittest.TestCase):
    
    def test_join_word_with_and(self):
        spam = ['apples', 'bananas', 'tofu', 'cats']
        expected_str = 'apples, bananas, tofu and cats'
        self.assertTrue(join_word_with_and(spam) == expected_str)

        spam = ['apples', 'bananas']
        expected_str = 'apples and bananas'
        self.assertTrue(join_word_with_and(spam) == expected_str)

        spam = ['apples']
        expected_str = 'apples'
        self.assertTrue(join_word_with_and(spam) == expected_str)

        spam = []
        expected_str = ''
        self.assertTrue(join_word_with_and(spam) == expected_str)


def join_word_with_and(input_list: list):
    new_str = ""
    if len(input_list) < 1:
        return(new_str)

    for i in range(len(input_list)):
        if i == 0:
            sep = ""
        elif i == len(input_list) - 1:
            sep = " and "
        else:
            sep = ", "
        new_str += f"{sep}{input_list[i]}"

    return(new_str)

if  __name__ == '__main__':
    import sys

    #unittest.main()
    #sys.exit()

    spam = ['apples', 'bananas', 'tofu', 'cats']
    #spam = ['apples', 'bananas']
    #spam = ['apples']

    print(join_word_with_and(spam))
