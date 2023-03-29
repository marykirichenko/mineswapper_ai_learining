from tkinter import *
import settings

class GameOver_Window:
    def close_app(self):
        settings.root.destroy()

    def __init__(self, win):
        self.topWindow = Toplevel()
        Label(self.topWindow, text="GAME OVER. YOU {}".format("WIN" if win == 1 else "LOST"),
              font=('Helvetica bold', 20)).pack(pady=10)
        Button(self.topWindow, text="Quit the game", width=10, command=self.close_app).pack()
        self.topWindow.geometry("400x120")
        self.topWindow.resizable(False, False)
        self.topWindow.attributes('-topmost', True)

