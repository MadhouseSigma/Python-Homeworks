import turtle as t
import numpy as np
from tkinter import Button
from tkinter import Tk


def penloc(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()


sudoko = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
sudoku = []
innerSudoku = []
allowedNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def possible(y, x, n):
    global sudoku
    for a in range(9):
        if sudoku[y][a] == n:
            return False
    for a in range(9):
        if sudoku[a][x] == n:
            return False
    y0 = (y // 3) * 3
    x0 = (x // 3) * 3
    for a in range(3):
        for b in range(3):
            if sudoku[y0 + a][x0 + b] == n:
                return False
    return True


def solve():
    global sudoku
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for n in range(10):
                    if possible(y, x, n):
                        sudoku[y][x] = n
                        solve()
                        sudoku[y][x] = 0
                return


def popSudoku(number):
    t.write(number, font=('Arial', 15, 'normal'))
    innerSudoku.append(int(number))
    t.fd(40)


# drawing the table
# starting parameters
t.pen(shown=False)
t.speed(0)
penloc(0, 250)
t.write(f'Sudoku Table with Random Numbers \nMade By Masoud Ghasemi', align='center')
penloc(180, 180)
t.pencolor("blue")
t.pensize(4)

# outer border
for i in range(4):
    t.right(90)
    t.forward(360)

# inner borders
t.pensize(2)
innerBorderLocation = [(-180, 60), (-180, -60), (-60, 180), (60, 180)]
for i in innerBorderLocation:
    if i[0] == -60:
        t.right(90)
    penloc(i[0], i[1])
    t.fd(360)


t.pencolor("black")
t.pensize(1)
# inner lines
for i in range(-140, 141, 40):
    if i in (-60, 60):
        continue
    penloc(i, 180)
    t.fd(360)

t.left(90)

for i in range(-140, 141, 40):
    if i in (-60, 60):
        continue
    penloc(-180, i)
    t.fd(360)


penloc(-164, 150)

t.pen(shown=True)
t.pu()
root = Tk()
root.geometry('350x50')

for i in range(1, 10):
    btn = Button(root, text=i, bd='1', command=popSudoku(i), padx='10', pady='10')
    btn.pack(side='left')
btn = Button(root, text='Empty', bd='1', command=popSudoku(0), padx='10', pady='10')
btn.pack(side='left')

root.mainloop()
root.

# t.write('9', font=('Arial', 15, 'normal'))
# for i in range(150, -171, -40):
#     for j in range(-164, 161, 40):
#         penloc(j, i)
#         inp = input('Enter Number for Shown Cell (Enter 0 for Empty Cell): ')
#         if inp in allowedNumbers:
#             innerSudoku.append(inp)
#         else:
#             inp = input('Wrong Input, Try Again\nEnter Number for Shown Cell (Enter 0 for Empty Cell): ')
#     sudoku.append(innerSudoku)
#     t.clear()
print(np.matrix(sudoku))
t.done()
