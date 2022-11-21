from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question = []

for line in question_data:
    question.append(Question(line["text"], line["answer"]))

quiz = QuizBrain(question)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")