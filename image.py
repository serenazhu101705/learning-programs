import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage

window = tk.Tk()
can = Canvas(window, height = 500, width = 1000, bg = 'white')
stack_ids = []
def click(event):
    x,y = (event.x)//50 * 50, (event.y)//50 * 50
    img = PhotoImage(master = can, file = '/home/serena/Pictures/nkc.png', name = '')
    can.create_image(x, y, anchor = 'center', image = img)
    stack_ids.append(img)
    print(x,y)
    print(img)

def bell(event):
    can.delete(stack_ids.pop())

can.focus_set()
can.bind("<Button-1>", click)
can.bind("<Delete>", bell)

can.pack()
window.mainloop()
