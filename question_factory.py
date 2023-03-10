import csv

from true_false_question import TrueFalseQuestion
from short_answer_question import ShortAnswerQuestion
from multiple_choice_question import MultipleChoiceQuestion
import time
import random
import db
import sqlite3



class QuestionFactory:
    @staticmethod
    def generate_question(question_type=None):
        """
        This method determines the question type and fetches the data
        necessary to create the question object
        :param question_type: String specifying question type
        :return: Question object
        """

        conn = sqlite3.connect('questions.db')
        c = conn.cursor()
        if question_type is None:
            question_types = ["TrueFalse", "ShortAnswer", "MultipleChoice"]
            question_type = random.choice(question_types)

        if question_type == "TrueFalse":
            c.execute("SELECT Question, Choices, Answer FROM TFquestions")
        elif question_type == "ShortAnswer":
            c.execute("SELECT Question, Choices, Answer FROM SAquestions")
        elif question_type == "MultipleChoice":
            c.execute("SELECT Question, Choices, Answer FROM MCquestions")


        row = c.fetchone()
        if not row:
            raise ValueError(f"No rows returned for question type {question_type}")
        question_data = tuple(row)
        question = QuestionFactory.get_question(question_type, *question_data)
        return question
    @staticmethod
    # def get_question_data(question_type):
    #     """
    #     This method fetches the data for the provided question type
    #     :param question_type: String representing one of the question types
    #     :return: question data for the question type
    #     """
    #     correct_answer = False
    #     answer_comment = "Joint Photographic Experts Group"
    #     question = "The initials JPEG stand for Jagged Point Enabled Graphs"
    #
    #     return question, correct_answer, answer_comment

    @staticmethod
    def get_question(question_type, *data):
        """
        This method creates a Question object based on the type and data
        provided.
        :param question_type: "TrueFalse", "ShortAnswer", or "MultipleChoice"
        :param data: optional data to add
        :return: Question object
        """

        if question_type == "TrueFalse":
            return TrueFalseQuestion(data[0], data[2])
        elif question_type == "ShortAnswer":
            return ShortAnswerQuestion(data[0], data[2])
        elif question_type == "MultipleChoice":
            choices = data[1].split("|")
            return MultipleChoiceQuestion(data[0], choices, data[2])
        else:
            raise TypeError("That is not a valid question type.")
        # if question_type == "TrueFalse":
        #     return TrueFalseQuestion(*data)
        # elif question_type == "ShortAnswer":
        #     return ShortAnswerQuestion(*data)
        # elif question_type == "MultipleChoice":
        #     return MultipleChoiceQuestion(*data)
        # else:
        #     raise TypeError("That is not a valid question type.")
        #
        # return TrueFalseQuestion(*data)


if __name__ == "__main__":
    qf = QuestionFactory()
    print(qf.generate_question("MultipleChoice"))
