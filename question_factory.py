from true_false_question import TrueFalseQuestion
from short_answer_question import ShortAnswerQuestion
from multiple_choice_question import MultipleChoiceQuestion


class QuestionFactory:
    def create_question(self, question_type, *data):
        """
        This method creates a Question object based on the type and data
        provided.
        :param question_type: "TrueFalse", "ShortAnswer", or "MultipleChoice"
        :param data: optional data to add
        :return: Question object
        """
        pass
