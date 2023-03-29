from tkinter import Button
import settings
import random
from gameOver import GameOver_Window

def get_surroundings(x, y):
    surrounding = []
    for cell in Cell.all:
        if cell.x >= x - 1 and cell.x <= x + 1 and cell.y >= y - 1 and cell.y <= y + 1:
            surrounding.append(cell)
    return surrounding


class Cell:
    all = []
    cells_left = int(settings.grid_size.split("x")[0]) ** 2

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        self.surrounding_cells_are_mines = []
        self.clicked = False
        Cell.all.append(self)

    def create_btn(self, cell_location):
        btn = Button(cell_location, width=2, height=1)
        btn.bind("<Button-1>", self.left_click_btn)
        btn.bind("<Button-3>", self.right_click_btn)
        self.cell_btn_object = btn

    def left_click_btn(self, event):
        if self.is_mine:
            self.explode()
        else:
            if len(list(filter(lambda cell: cell.is_mine == True, get_surroundings(self.x, self.y)))) == 0:
               for cell in get_surroundings(self.x, self.y):
                   cell.show_cell_info()
                   cell.cell_btn_object.configure(bg='#8c8c8c')
                   if cell.clicked == False:
                       Cell.cells_left = Cell.cells_left - 1
                       cell.clicked = True
            else:
                self.show_cell_info()
                self.clicked = True
                Cell.cells_left -= 1
                self.cell_btn_object.configure(bg='#8c8c8c')
        print(Cell.cells_left,settings.amount_of_bombs )
        if Cell.cells_left == int(settings.amount_of_bombs):
            self.game_over = GameOver_Window(1)
            self.game_over.topWindow.grab_set()

    def explode(self):
        self.cell_btn_object.configure(bg='black')
        self.game_over = GameOver_Window(0)
        self.game_over.topWindow.grab_set()

    def show_cell_info(self):
        self.surrounding_cells_are_mines  = list(filter(lambda cell: cell.is_mine == True, get_surroundings(self.x, self.y)))
        self.cell_btn_object['text'] = len(self.surrounding_cells_are_mines )


    def right_click_btn(self, event):
        if(self.clicked== False):
            if self.cell_btn_object.cget('bg') == 'red':
                self.cell_btn_object.configure(bg='#f0f0f0')
            else:
                self.cell_btn_object.configure(bg='red')

    def isMines(amount_of_mines):
        mine_cells = random.sample(Cell.all, amount_of_mines)
        for mine_cell in mine_cells:
            mine_cell.is_mine = True
        print(mine_cells)
