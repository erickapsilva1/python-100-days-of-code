from question_model import Question
from data import question_data

question = []
i = 0

for line in question_data:
    question.append(Question(line["text"], line["answer"]))

print(question[0].text)