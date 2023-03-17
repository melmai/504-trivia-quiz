from true_false_question import TrueFalseQuestion
from short_answer_question import ShortAnswerQuestion
from multiple_choice_question import MultipleChoiceQuestion
import random
import sqlite3


class QuestionFactory:
    def __init__(self):
        self.__tf_stack = []
        self.__mc_stack = []
        self.__sa_stack = []
        self.__fill_stack()

    def __fill_stack(self):
        conn = sqlite3.connect('questions.db')
        c = conn.cursor()
        c.execute('SELECT * FROM TFquestions')
        self.__tf_stack = c.fetchall()
        random.shuffle(self.__tf_stack)
        c.execute('SELECT * FROM MCquestions')
        self.__mc_stack = c.fetchall()
        random.shuffle(self.__mc_stack)
        c.execute('SELECT * FROM SAquestions')
        self.__sa_stack = c.fetchall()
        random.shuffle(self.__sa_stack)

    def generate_question(self, question_type=None):
        """
        This method determines the question type and fetches the data
        necessary to create the question object
        :param question_type: String specifying question type
        :return: Question object
        """

        if question_type is None:
            question_types = ["TrueFalse", "ShortAnswer", "MultipleChoice"]
            question_type = random.choice(question_types)
        if question_type == "TrueFalse":
            if self.__tf_stack:
                question_data = self.__tf_stack.pop()
                return TrueFalseQuestion(question_data[1], question_data[3])
            else:
                raise ValueError('error no more questions')
        elif question_type == "ShortAnswer":
            if self.__sa_stack:
                question_data = self.__sa_stack.pop()
                return ShortAnswerQuestion(question_data[1], question_data[3])
            else:
                raise ValueError('error no more questions')
        elif question_type == "MultipleChoice":
            if self.__mc_stack:
                question_data = self.__mc_stack.pop()
                return MultipleChoiceQuestion(question_data[1], question_data[2], question_data[3])
            else:
                raise ValueError('error no more questions')



    @staticmethod
    def mock(question_type):
        if question_type == "ShortAnswer":
            return ShortAnswerQuestion.mock()
        elif question_type == "TrueFalse":
            return TrueFalseQuestion.mock()
        elif question_type == "MultipleChoice":
            return MultipleChoiceQuestion.mock()
        else:
            raise ValueError("That's not a valid question type.")


if __name__ == "__main__":
    print(QuestionFactory.mock("TrueFalse"))
    print(QuestionFactory.mock("MultipleChoice"))
    print(QuestionFactory.mock("ShortAnswer"))
