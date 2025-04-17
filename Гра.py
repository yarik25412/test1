import tkinter as tk
import random
from tkinter import messagebox

GRID_SIZE = 6
BOMB_COUNT = 3

class ThinkerGrid:
    def __init__(self, master):
        self.master = master
        self.master.title("Thinker Grid 🧠")
        self.buttons = []
        self.bomb_pos = random.sample(range(GRID_SIZE * GRID_SIZE), BOMB_COUNT)

        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                btn = tk.Button(master, width=6, height=3,
                                command=lambda i=i, j=j: self.check_cell(i, j))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

    def check_cell(self, i, j):
        index = i * GRID_SIZE + j
        if index in self.bomb_pos:
            self.buttons[i][j].configure(text="💣", bg="red", state="disabled")
            self.end_game(False)
        else:
            self.buttons[i][j].configure(text="✓", bg="lightgreen", state="disabled")

    def end_game(self, won):
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")
        if won:
            messagebox.showinfo("Thinker Grid", "Ви перемогли!")
        else:
            messagebox.showinfo("Thinker Grid", "Ви натрапили на бомбу!")

if __name__ == "__main__":
    root = tk.Tk()
    game = ThinkerGrid(root)
    root.mainloop()
