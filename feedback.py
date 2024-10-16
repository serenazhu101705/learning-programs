import tkinter as tk
import string
from tkinter import *
from tkinter import messagebox

window = tk.Tk()
window.title("HARRY FEEDBACK")

def handle_keypress(event):
    if len(text_box.get('1.0',tk.END)) == 2 and event.char == '\x08':
        submit_btn['state'] = 'disabled'
    else:
        submit_btn['state'] = 'normal'
    letters = list(string.printable)        
    if len(text_box.get('1.0',tk.END)) == 1 and event.char not in letters:
        submit_btn['state'] = 'disabled'

    
lbl = tk.Label(window, text="Please type your feedback below.")
lbl.pack()
text_box = tk.Text()
text_box.pack()
text_box.bind("<Key>",handle_keypress)

def submit():
    submit_btn['text'] = 'SUBMITTED'
    submit_btn['state'] = 'disabled'
    res = text_box.get("1.0",tk.END)
    f = open("../personal assistant/feedback.txt",'a')
    f.write("\n")
    f.write(res)
    f.close()
    messagebox.showinfo("Feedback","Thank you for your feedback! We'll get back to you ASAP.")
    window.destroy()
    

submit_btn = tk.Button(window, text="SUBMIT",command=submit, state='disabled')
submit_btn.pack()

window.mainloop()


