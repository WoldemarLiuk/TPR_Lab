from tkinter import *
import tkinter as tk

from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import numpy as np

root = Tk()

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 225
h = h - 225
root.geometry('440x300+{}+{}'.format(w, h))
root.title("Прийняття рішень в умовах невизначенності і ризику")

showinfo(
        title='Оберіть файл з матрицею',
        message='Будь ласка, оберіть файл з матрицею!'
    )

filetypes = (
    ('text files', '*.txt'),
    ('All files', '*.*')
)

filename = fd.askopenfilename(
    title='Відкрити файл',
    initialdir='/',
    filetypes=filetypes)

class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=10, font=('Arial', 10))
                self.e.grid(row=i, column=j, padx=10, pady=10)
                self.e.insert(END, lst[i][j])

lst = np.loadtxt(filename, dtype='i', delimiter=',')

total_rows = len(lst)
total_columns = len(lst[0])
t = Table(root)

def count():

    lst = np.loadtxt(filename, dtype='i', delimiter=',')
    minimum = np.min(lst, axis=1)
    maximum = np.max(lst, axis=1)

    avg = np.average(lst, axis=1)
    suma = np.sum(lst, axis=1)

    # Вальд
    vald = np.max(minimum)
    vald_opt = np.where(minimum == np.amax(minimum))
    vald_opt1 = np.min(vald_opt) + 1
    vald_opt2 = np.max(vald_opt) + 1

    # Лаплас
    laplas = np.max(avg)
    laplas = round(laplas, 1)
    laplas_opt = np.where(avg == np.amax(avg))
    laplas_opt = np.min(laplas_opt) + 1

    # Гурвіц
    k = 0.6
    r = k*minimum+(1-k)*maximum
    gurwiz = np.max(r)
    gurwiz_opt = np.where(r == np.amax(r))
    gurwiz_opt = np.min(gurwiz_opt) + 1

    #визначення оптимальної стратегії в умовах невизначеності
    strategy_nevysnach = [vald_opt1, vald_opt2, laplas_opt, gurwiz_opt]
    opt_strategy_nevysnach = max(strategy_nevysnach, key=strategy_nevysnach.count)

    # Байес-Лаплас
    p1 = 0.55
    p2 = 0.3
    p3 = 0.15

    r1 = p1*suma[0]
    r2 = p2*suma[1]
    r3 = p3*suma[2]

    b_l = [r1, r2, r3]
    b_l_max = np.max(b_l)
    b_l_opt = b_l.index(b_l_max)+1
    b_l_max = round(b_l_max, 1)

    text1.delete("1.0", END)
    text1.insert("1.0", b_l_opt)
    text1.insert("1.0", '\nВ умовах ризику оптимальною є стратегія №')
    text1.insert("1.0", b_l_opt)
    text1.insert("1.0", ', стратегія №')
    text1.insert("1.0", b_l_max)
    text1.insert("1.0", '\nКритерій Байеса-Лапласа: ')
    text1.insert("1.0", '\n\nПрийняття рішення в умовах ризику:')

    text1.insert("1.0", opt_strategy_nevysnach)
    text1.insert("1.0", '\nВ умовах невизначеності оптимальною є стратегія №')
    text1.insert("1.0", gurwiz_opt)
    text1.insert("1.0", ', стратегія №')
    text1.insert("1.0", gurwiz)
    text1.insert("1.0", '\nКритерій Гурвіца: ')

    text1.insert("1.0", laplas_opt)
    text1.insert("1.0", ', стратегія №')
    text1.insert("1.0", laplas)
    text1.insert("1.0", '\nКритерій Лапласа: ')

    text1.insert("1.0", vald_opt2)
    text1.insert("1.0", ',')
    text1.insert("1.0", vald_opt1)
    text1.insert("1.0", ', стратегії №')
    text1.insert("1.0", vald)
    text1.insert("1.0", '\nКритерій Вальда: ')
    text1.insert("1.0", 'Прийняття рішення в умовах невизначеності:')

labelframe = LabelFrame(root, text="Розв'язок", width=420, height=175)
labelframe.place(x=10, y=120)

text1 = tk.Text(width=50, height=9)
text1.place(x=15, y=140)

b1 = tk.Button(text="Обчислити", command=count).place(x=320, y=47)

root.mainloop()