from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    quest_text = question["question"]
    quest_answ = question["correct_answer"]
    question_bank.append(Question(quest_text, quest_answ))

quiz = QuizBrain(question_bank)

continue_game = True
while continue_game:
    quiz.next_question()
    continue_game = quiz.still_has_questions()
print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
