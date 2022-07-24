from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
CANVAS_COLOR = "#FFFFFF"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        self.canvas = Canvas(self.window, width=300, height=250, bg=CANVAS_COLOR)
        self.text = self.canvas.create_text(150, 125, width=280, text="Sample Text", 
                                font=("Arial", 20, "italic"), justify="left")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="#FFFFFF", font=("Arial", 14, "bold"))
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img= PhotoImage(file="images/false.png")

        self.true_button = Button(self.window, image=self.true_img, bd=0,
                            bg=THEME_COLOR, highlightthickness=0, command=self.true_func)
        self.true_button.grid(column=0,row=2, padx=20, pady=20)
        
        self.false_button = Button(self.window, image=self.false_img, bd=0,
                            bg=THEME_COLOR, highlightthickness=0, command=self.false_func)
        self.false_button.grid(column=1,row=2, padx=20, pady=20)
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text, text=q_text)
    
    def true_func(self):
        self.quiz.check_answer("true")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.check_next_question()

    def false_func(self):
        self.quiz.check_answer("false")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.check_next_question()

    def check_next_question(self):
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.canvas.itemconfig(self.text, 
            text=f"Congratualations you've finished the quiz!\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
        
