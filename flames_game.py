import tkinter as tk
from tkinter import messagebox, ttk
import string

window = tk.Tk()
window.title("Flames Game")

bg_color = 'white'
fg_color = 'black'

window.configure(bg = bg_color)
window.geometry('300x200')

heading= tk.Label(window, text='Type in 2 people below', bg = bg_color)
heading.grid(row = 0, column = 3)

person_1 = tk.Entry(window)
person_1.grid(row = 2, column = 3)
lbl_1 = tk.Label(window, text = 'Person 1', bg = bg_color, fg = fg_color)
lbl_1.grid(row = 2, column = 2)

person_2 = tk.Entry(window)
person_2.grid(row = 4, column = 3)
lbl_2 = tk.Label(window, text = 'Person 2', bg = bg_color, fg = fg_color)
lbl_2.grid(row = 4, column = 2)

r_lbl = tk.Label(window, bg = bg_color, fg = fg_color)
r_lbl.grid(row = 6, column = 3)

p = ttk.Progressbar(window, length = 200)
p.grid(row = 7, column = 3)

p_lbl = tk.Label(window, bg = bg_color, fg = fg_color, text = "Hate                                   Love")
p_lbl.grid(row = 8, column = 3)

def submit():
    global r_lbl
    r_lbl.grid_forget()
    if len(person_1.get() + person_2.get()) == 0:
        ...
    else:
        prs_1 = person_1.get().lower()
        prs_2 = person_2.get().lower()
        person_1.delete(0, tk.END)
        person_2.delete(0, tk.END)
        number = 0
        for i in prs_1:
            if i in 'flames':
                number = number + 1
        for i in prs_2:
            if i in 'flames':
                number = number + 1
        flames = list('flames')
        if number % 6 == 0 or number == 0:
            if number != 0:
                r = flames[5]
            else:
                r = 'none'
        else:
            r = flames[number % 6 - 1]
        relations = {'f':'Friends','l':'Lovers','a':'Affectionate','m':'Marriage','e':'Enemies','s':'Siblings','none':'None'}
        values = {'f':70, 'l': 95, 'a': 60, 'm': 100, 'e': 2, 's': 80, 'none':0}
        r_lbl = tk.Label(window, text = 'Relationship Status: %s' % relations[r], bg = bg_color, fg = fg_color)
        r_lbl.grid(row = 6, column = 3)
        p['value'] = values[r]
        submit_btn['state'] = 'disabled'
        
submit_btn = tk.Button(window, text = "SUBMIT", command = submit, state = 'disabled', bg = bg_color, fg = fg_color)
submit_btn.grid(row = 5, column = 3)


def enter(event):
    if event.char == '\r':
        global submit
        submit()

def handle_keypress(event):
    if len(person_2.get()) == 2 and event.char == '\x08':
        submit_btn['state'] = 'disabled'
    else:
        submit_btn['state'] = 'normal'
    letters = list(string.printable)        
    if len(person_2.get()) == 1 and event.char not in letters or len(person_2.get()) == 0 and event.char not in letters :
        submit_btn['state'] = 'disabled'
    if len(person_2.get()) == 0 and event.char == '\t':
        submit_btn['state'] = 'disabled'

submit_btn.bind("<Key>",enter)
person_2.bind("<Key>", handle_keypress)
