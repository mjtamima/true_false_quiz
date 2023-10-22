from question_model import Question
from quiz_brain import QuizBrain
from data_new import data

question_bank = []
for item in data:
    question = Question(item['question'], item['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
