from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question(data['question'], data['correct_answer']))

Quiz = QuizBrain(question_bank)
while Quiz.still_has_questions():
    Quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was {Quiz.score}/{Quiz.question_number}")

