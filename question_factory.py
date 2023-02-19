from true_false_question import TrueFalseQuestion
from short_answer_question import ShortAnswerQuestion
from multiple_choice_question import MultipleChoiceQuestion


class QuestionFactory:
    @staticmethod
    def create_question(question_type, *data):
        """
        This method creates a Question object based on the type and data
        provided.
        :param question_type: "TrueFalse", "ShortAnswer", or "MultipleChoice"
        :param data: optional data to add
        :return: Question object
        """
        if question_type == "TrueFalse":
            return TrueFalseQuestion(*data)
        elif question_type == "ShortAnswer":
            return ShortAnswerQuestion(*data)
        elif question_type == "MultipleChoice":
            return MultipleChoiceQuestion(*data)
        else:
            raise TypeError("That is not a valid question type.")
