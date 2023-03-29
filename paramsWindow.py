from tkinter import *
import settings

class ParamWindow:
    field_size = [
        '6x6',
        '8x8',
        '10x10',
        '12x12',
        '14x14',
    ]

    def pass_to_settings(self):
        settings.amount_of_bombs = self.entry.get()
        settings.grid_size = self.variable.get()
        print(settings.amount_of_bombs, settings.grid_size)
        self.topWindow.destroy()

    def __init__(self):
        self.topWindow = Toplevel()
        self.topWindow.title('Options')
        Label(self.topWindow, text="Choose the size of the field and amount of bombs",
              font=('Helvetica bold', 10)).pack(pady=20)
        self.topWindow.geometry("300x300")
        self.variable = StringVar(self.topWindow)
        self.variable.set(self.field_size[0])
        w = OptionMenu(self.topWindow, self.variable, *self.field_size)
        w.pack()
        Label(self.topWindow, text="Amount of bombs",
              font=('Helvetica bold', 10)).pack(pady=20)
        self.entry = Entry(self.topWindow, width=20)
        self.entry.focus_set()
        self.entry.pack()
        Button(self.topWindow, text="Apply", width=10, command=self.pass_to_settings).pack(pady=20)
        self.topWindow.resizable(False, False)
        self.topWindow.attributes('-topmost', True)
