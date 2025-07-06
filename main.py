from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    question_bank.append(Question(questions["question"], questions["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.check_answer()

print("Quiz Completed!")
print(f"Your Final Score is {quiz.score}/10")
