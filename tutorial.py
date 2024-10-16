import tkinter as tk
from tkinter.ttk import *

bg_color, fg_color = "white", "black"
window = tk.Tk()
window.title("HARRY TUTORIAL")
window.configure(bg = bg_color)
frame = tk.Frame(window)
frame.grid(row = 3,column = 4)


lbl = tk.Label(master = window,text = "Press START to start the tutorial.",bg=bg_color,fg=fg_color)
lbl.grid(row=0, column=4)
value = -1
harrys = ["Welcome to the Serena Zhu TM personal assistant\nonce-in-a-lifetime experience!\nIt's time to meet your assistant. Say hello, Harry!",
        "Harry TM is a highly-intelligent artificial intelligence machine\n that can understand simple and more complex commands\nordered by the user.",
          "In this tutorial, we'll walk through\nsome basic commands and responses.\nSit back, and enjoy as we let harry take over the show!",
          "To start the personal assistant, you must first give it a name.\nIf you press ENTER without any response, it will automatically\ncall itself Harry. Next, you must\nenter a name for yourself. Any name\nis acceptable.",
          "Afterwards, Harry will give you a short introduction that\ntells you how to see a list\nof options to ask him and how to exit\nthe assistant. Once you type\nin \"Goodbye, Harry.\", it will automatically save your\nname and it's name as well. To change\nyour name, simply ask, \"Harry, can I change my name?\".\nThe same can be said to change the assistant's name",
          "Harry can also tell you the time, the date, the weather,\nthe daily news, a joke, and others.\nIt can open a web browser and, using our new web scraping technology,\ngive you a brief summary of your favorite celebirites.\nEx. \"Harry, who is Justin Bieber?\". The abilities of\nHarry don't stop there. It can also show\nrecipes to cook for your next delicious dinner,\nsearch images on the web, tell you the most popular people on the internet,\nand who has a birthday today and tomorrow.\nFeel free to play around and explore!",
          "We have been getting numerous reports\nabout failed internet connection. This is likely due to the\nMyCircle time limit set on this\ncomputer. To get more time online,\ncontact Josh Zhu at Home Office for support. If it still\ndoes not connect, try checking the\nGeekHub connection and wait to try again.",
          "If you are experiencing any other difficulties,\nplease contact Serena Zhu TM Co.\nwith concerns and we will get back to\nyou as soon as possible.",
          "We hope you enjoy our very first personal assistant machine\nand wish you well as you get to\nknow our wonderful assistant!"]

def Next():
    global value
    value = value + 1
    if value == 0:
        start_btn.grid_forget()
        skip_lbl.grid(row=0,column=0, sticky="nsew")
        ok_btn.grid(row=2,column=0, sticky="nsew")
        next_btn.grid(row=1, column=5, sticky="nsew")
        prev_btn.grid(row=1, column=3, sticky="nsew")
        combo.grid(row=1,column=0, sticky="nsew")
    if value == 1:
        prev_btn["state"] = "normal"
    if value == len(harrys):
        window.destroy()
    else:
        slide = harrys[value]
        lbl["text"] = f"{slide}"
    if value == len(harrys) - 1:
        next_btn["text"] = "EXIT"
        
def Previous():
    global value
    value = value - 1
    if value == -1 or value == 0:
        prev_btn["state"] = 'disabled'
        value = 0
    if value == -2:
        lbl["text"] = lbl["text"]
        value = -1
    else:
        slide = harrys[value]
        lbl["text"] = f"{slide}"
    if value == len(harrys) - 2:
        next_btn["text"] = "NEXT"

def ok():
    global value
    value = int(combo.get()) - 1
    if value < 0:
        value = 0
    if value > len(harrys) - 1:
        value = len(harrys) - 1
    if value > 0:
        prev_btn['state'] = 'normal'
    if value == 0:
        prev_btn['state'] = 'disabled'
    if value == len(harrys) - 1:
        next_btn['text'] = 'EXIT'
    else:
        next_btn['text'] = 'NEXT'
    slide = harrys[value]
    lbl["text"] = f"{slide}"
    combo.delete(0, tk.END)
        


next_btn = tk.Button(master=window,text="NEXT",command=Next,bg=bg_color,fg=fg_color)
prev_btn = tk.Button(master=window, text="PREVIOUS",command=Previous,state='disabled',bg=bg_color,fg=fg_color)
start_btn = tk.Button(master=window, text="START",command=Next,bg=bg_color,fg=fg_color)
start_btn.grid(row=1,column=4,sticky='nsew')
skip_lbl = tk.Label(frame, text="Go to slide...", fg=fg_color)
combo = Combobox(frame, width=5,height=5)
combo['values'] = tuple([i for i in range(1,len(harrys) + 1)])
ok_btn = tk.Button(frame, text="OK", command=ok, width=1,height=1, bg=bg_color,fg=fg_color)

window.mainloop()
