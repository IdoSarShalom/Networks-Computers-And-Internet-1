# ******************************
# Tomer Griba 325105625
# Ido Sar Shalom 212410146
# ******************************
from random import randrange
from random import random


class Question:
    def __init__(self, _question, _ans1, _ans2, _ans3, _ans4, _correct_ans_index):

        self.ans_list = [_ans1, _ans2, _ans3, _ans4]
        self.correct_ans_index = _correct_ans_index - 1
        self.question = _question

    def get_question(self):

        return str(self.question) + "\n" + "1. " + str(self.ans_list[0]) + "\n" + \
               "2. " + str(self.ans_list[1]) + "\n" + \
               "3. " + str(self.ans_list[2]) + "\n" + \
               "4. " + str(self.ans_list[3]) + "\n"

    # eliminate 2 wrong answers from the question and return it
    def get_help_question(self):
        rand_num = randrange(4)
        while rand_num == self.correct_ans_index:
            rand_num = randrange(4)

        if random() < 0.5:
            str1 = self.question + "\n" + "1. " + str(self.ans_list[self.correct_ans_index]) + "\n" + "2. " + str(
                self.ans_list[rand_num])
            self.correct_ans_index = 0
            return str1
        else:
            str1 = self.question + "\n" + "1. " + str(self.ans_list[rand_num]) + "\n" + "2. " + str(
                self.ans_list[self.correct_ans_index])
            self.correct_ans_index = 1
            return str1

    def is_correct_answer(self, ans_index):
        return ans_index == self.correct_ans_index + 1

