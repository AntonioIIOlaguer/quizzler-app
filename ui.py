from tkinter import *
THEME_COLOR = "#375362"
CANVAS_COLOR = "#FFFFFF"

class QuizInterface():

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        self.canvas = Canvas(self.window, width=300, height=250, bg=CANVAS_COLOR)
        self.text = self.canvas.create_text(150, 125, text="Sample Text", font=("Arial", 20, "italic"), justify="left")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="#FFFFFF", font=("Arial", 14, "bold"))
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img= PhotoImage(file="images/false.png")

        self.true_button = Button(self.window, image=self.true_img, bd=0, bg=THEME_COLOR, highlightthickness=0)
        self.true_button.grid(column=0,row=2, padx=20, pady=20)
        
        self.false_button = Button(self.window, image=self.false_img, bd=0, bg=THEME_COLOR, highlightthickness=0)
        self.false_button.grid(column=1,row=2, padx=20, pady=20)
        self.window.mainloop()