import sqlite3
import requests
import json

response = requests.get("https://opentdb.com/api.php?amount=50&type=multiple")
json_data = json.loads(response.text)

con = sqlite3.connect('questions.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS questions
                (question_type TEXT, question TEXT, choices TEXT, correct_answer TEXT)''')

for question in json_data['results']:
    question_type = question['type']
    question_text = question['question']
    choices = ",".join([str(choice) for choice in question['incorrect_answers']] + [str(question['correct_answer'])])
    correct_answer = question['correct_answer']
    cur.execute("INSERT INTO questions (question_type, question, choices, correct_answer) VALUES (?, ?, ?, ?)",
                (question_type, question_text, choices, correct_answer))

con.commit()

