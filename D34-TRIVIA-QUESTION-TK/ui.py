THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        self.score = Label(text="Score: 0", font=("Arial", 15, "normal"), background=THEME_COLOR, foreground="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some question text", width= 280, font=("Arial", 20, "italic"))
        self.canvas.grid(columnspan=2, column=0, row=1, pady=50)

        wrong_img = PhotoImage(file='./images/false.png', width=100, height=97)
        self.wrong_button =Button(image=wrong_img, highlightthickness=0, command=self.wrong_pressed)
        self.wrong_button.grid(row=4, column=0)

        right_img = PhotoImage(file='./images/true.png', width=100, height=97)
        self.right_button =Button(image=right_img, highlightthickness=0, command=self.right_pressed)
        self.right_button.grid(row=4, column=1)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
        else:
            self.canvas.itemconfigure(self.question_text, text="You have reached the end")
            self.right_button.configure(state="disabled")
            self.wrong_button.configure(state="disabled")

    def right_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):    
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.next_question)