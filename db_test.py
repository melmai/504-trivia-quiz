import sqlite3
import unittest


class dbtest(unittest.TestCase):
    def test_db_connection(self):
        """This method tests the ability to connect to the questions
        database"""
        con = sqlite3.connect('questions.db')
        self.assertIsNot(con, 'not_existent.db')

    def test_tf_db(self):
        """This method tests the ability to pull a true or false question
        and answer from the questions database"""
        con = sqlite3.connect('questions.db')
        self.assertIsNotNone(con, "couldn't connect to db")
        # self.assertEqual()
        c = con.cursor()
        c.execute('SELECT Question FROM TFquestions')
        result = c.fetchone()
        expected = (
            'True or False: New York City is composed of between 36 and 42 '
            'islands.',)
        c.execute('SELECT Answer FROM TFquestions')
        answer_result = c.fetchone()
        answer_expected = ('true',)
        self.assertEqual(result, expected)
        self.assertEqual(answer_result, answer_expected)
        c.close()

    def test_mc_db(self):
        """This method tests the ability to pull a multiple choice question
        and answer from the questions database"""
        con = sqlite3.connect('questions.db')
        self.assertIsNotNone(con, "couldn't connect to db")
        # self.assertEqual()
        c = con.cursor()
        c.execute('SELECT Question FROM MCquestions')
        result = c.fetchone()
        expected = ("What's the largest bone in the human body?\n\n",)
        c.execute('SELECT Answer FROM MCquestions')
        answer_result = c.fetchone()
        answer_expected = ('femur',)
        self.assertEqual(result, expected)
        self.assertEqual(answer_result, answer_expected)
        c.close()

    def test_sa_db(self):
        """This method tests the ability to pull a short answer question and
        answer from the questions database"""

        con = sqlite3.connect('questions.db')
        self.assertIsNotNone(con, "couldn't connect to db")
        c = con.cursor()
        c.execute('SELECT Question FROM SAquestions')
        result = c.fetchone()
        expected = (
            "Short answer: In chess, what direction can a bishop move?",)
        c.execute('SELECT Answer FROM SAquestions')
        answer_result = c.fetchone()
        answer_expected = ('diagonally',)
        self.assertEqual(result, expected)
        self.assertEqual(answer_result, answer_expected)
        c.close()


if __name__ == '__main__':
    unittest.main()
