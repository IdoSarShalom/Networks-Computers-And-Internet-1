# ******************************
# Tomer Griba 325105625
# Ido Sar Shalom 212410146
# ******************************
# import the module question
from question import *
from random import randrange


class QuestionsPool:
    def __init__(self):
        self.num_of_questions = 15
        self.question_list = [Question("Who invented apple?:", "Mark Zuckerberg", "Steve Jobs", "Tim Cook", "Bill Gates", 2),
                              Question("What is the largest country in the world?", "Russia", "China", "Canada", "Israel", 1),
                              Question("What is the capital city of Italy?", "Tokyo", "Rome", "Paris", "Berlin", 2),
                              Question("How many stars are on the American flag?", "52", "49", "35", "50", 4),
                              Question("What is the square root of 441?", "21", "22", "16", "19", 1),
                              Question("How old is the earth estimated to be?", "8.5 billion years", "1 billion years", "4.5 billion years", "6 billion years", 3),
                              Question("How do you say 'Hello' in spanish?", "ciao", "hola", "bonjour", "sveiki", 2),
                              Question("What is the capital city of Peru?", "Washington", "Lima", "San Marino", "Minsk", 2),
                              Question("Which planet is the farthest from the sun?", "Pluto", "Neptune", "Venus", "Mars", 2),
                              Question("Solve the equation: (-1)-2+3x4+(-3)x2", "18", "-6", "3", "0", 3),
                              Question("Which of the following countries does not border with Italy?", "Switzerland", "France", "Austria", "Germany", 4),
                              Question("How many countries are there in the United Nations?","193","207","151","163",1),
                              Question("What is the world record for typing?","212 wpm","231 wpm","201 wpm","248 wpm",1),
                              Question("How many times have brazil won the world cup?","4","1","5","7",3),
                              Question("How many times have israel qualified for the world cup?","4","0","1", "2", 3)]

    def randomize_question(self):

        # Randomize a number between 0 to num_of_questions-1
        rand_num = randrange(self.num_of_questions)

        returned_object = self.question_list[rand_num]

        # Delete previous question
        del self.question_list[rand_num]

        self.num_of_questions = self.num_of_questions - 1

        return returned_object




