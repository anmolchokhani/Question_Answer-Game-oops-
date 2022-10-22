from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for item in question_data:
    data_question = item["text"]
    data_answer= item["answer"]
    question_bank.append(Question(data_question,data_answer))

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
