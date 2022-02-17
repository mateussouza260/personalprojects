from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question", font=("Arial", 15, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Button - TRUE
        right_img = PhotoImage(file="./images/true.png")
        self.button_right = Button(image=right_img, command=self.true_button, highlightthickness=0)
        self.button_right.grid(column=0, row=2)

        # Button - FALSE
        wrong_img = PhotoImage(file="./images/false.png")
        self.button_wrong = Button(image=wrong_img, command=self.false_button, highlightthickness=0)
        self.button_wrong.grid(column=1, row=2)

        # Label - SCORE
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
