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

        # # read contents of db and put it inside the list, can be 1 or 3
        # conn = sqlite3.connect('questions.db')
        # c = conn.cursor()
        # if question_type is None:
        #     question_types = ["TrueFalse", "ShortAnswer", "MultipleChoice"]
        #     question_type = random.choice(question_types)
        # # keep track of which questions have been asked. grab all questions from db and add to a list. shuffle list
        # if question_type == "TrueFalse":
        #     c.execute("SELECT DISTINCT Question, Choices, Answer FROM TFquestions")
        # elif question_type == "ShortAnswer":
        #     c.execute("SELECT DISTINCT Question, Choices, Answer FROM SAquestions")
        # elif question_type == "MultipleChoice":
        #     c.execute("SELECT DISTINCT Question, Choices, Answer FROM MCquestions")
        #
        # row = c.fetchall()
        # #fetchone is the reason I keep getting the same question.
        # if not row:
        #     raise ValueError(f"No rows returned for question type {question_type}")
        # question_data = tuple(row)
        # question = QuestionFactory.get_question(question_type, *question_data) #not good oo
        # return question

    # @staticmethod
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
            choices = data[1].split(",")
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

    # print(QuestionFactory.generate_question("TrueFalse"))
