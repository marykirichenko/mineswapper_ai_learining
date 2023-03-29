from tkinter import *
import settings
from cell import Cell
from paramsWindow import ParamWindow


class MainWindow:
    def __init__(self):
        print("Building App")
        self.root = Tk()
        self.root['bg'] = 'gray'
        self.root.title('Minesweeper')
        self.root.geometry(f'{settings.mainWin_width}x{settings.mainWin_height}')
        self.root.resizable(False, False)
        self.param_window = ParamWindow()
        settings.root = self.root
        self.root.wait_window(self.param_window.topWindow)
        menu = Frame(self.root, bg="#A9A9A9", width=settings.mainWin_width, height=50)
        menu.place(x=0, y=0)
        self.createGrid()
        self.root.mainloop()

    def createGrid(self):
        gameField = Frame(self.root, bg="black", width=f'{settings.mainWin_width * 0.75}',
                          height=f'{settings.mainWin_height * 0.75}')
        gameField.place(x=f'{settings.mainWin_width * 0.125}', y=80)
        for i in range(int(settings.grid_size.split("x")[0])):
            for j in range(int(settings.grid_size.split("x")[0])):
                c = Cell(x=i, y=j)
                c.create_btn(gameField)
                c.cell_btn_object.grid(column=i, row=j)
        Cell.isMines(int(settings.amount_of_bombs))
        for cell in Cell.all:
            print(cell.is_mine)

a = MainWindow()
