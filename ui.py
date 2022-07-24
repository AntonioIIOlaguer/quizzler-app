from tkinter import *
THEME_COLOR = "#375362"
CANVAS_COLOR = "#FFFFFF"

class QuizInterface():

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(self.window, width=300, height=250, bg=CANVAS_COLOR)
        self.window.mainloop()