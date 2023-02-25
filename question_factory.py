from true_false_question import TrueFalseQuestion
from short_answer_question import ShortAnswerQuestion
from multiple_choice_question import MultipleChoiceQuestion
import random


class QuestionFactory:
    @staticmethod
    def generate_question(question_type=None):
        """
        This method determines the question type and fetches the data
        necessary to create the question object
        :param question_type: String specifying question type
        :return: Question object
        """

        if not question_type:  # generate random question if not specified
            question_types = ["TrueFalse", "ShortAnswer", "MultipleChoice"]
            question_type = random.choice(question_types)

        question, answer, q_data = QuestionFactory.get_question_data(
            question_type)
        return QuestionFactory.get_question(question_type, question, answer,
                                            q_data)

    @staticmethod
    def get_question_data(question_type):
        """
        This method fetches the data for the provided question type
        :param question_type: String representing one of the question types
        :return: question data for the question type
        """
        correct_answer = False
        answer_comment = "Joint Photographic Experts Group"
        question = "The initials JPEG stand for Jagged Point Enabled Graphs"

        return question, correct_answer, answer_comment

    @staticmethod
    def get_question(question_type, *data):
        """
        This method creates a Question object based on the type and data
        provided.
        :param question_type: "TrueFalse", "ShortAnswer", or "MultipleChoice"
        :param data: optional data to add
        :return: Question object
        """
        # if question_type == "TrueFalse":
        #     return TrueFalseQuestion(*data)
        # elif question_type == "ShortAnswer":
        #     return ShortAnswerQuestion(*data)
        # elif question_type == "MultipleChoice":
        #     return MultipleChoiceQuestion(*data)
        # else:
        #     raise TypeError("That is not a valid question type.")

        return TrueFalseQuestion(*data)


if __name__ == "__main__":
    qf = QuestionFactory()
    q = qf.generate_question()
    print(q.question)
    print(q.answer)
    print(q.comment)
