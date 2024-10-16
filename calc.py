import tkinter as tk

window = tk.Tk()
window.title("SZ 1.0")

def submit(event):
    opers = {"x": [int.__mul__, 1], "/": [int.__truediv__, 2], "+": [int.__add__, 3], "-": [int.__sub__, 4]}
    s = [i for i in opers if i in e.get()]
    j = lambda st: opers[st][1]; s.sort(key = j)

    first = int(e.get().split(s[0])[0])
    
    lbl['text'] = a
    
def insert(s):
    e.insert(tk.END, s)
e = tk.Entry(window, width = 25)
lbl = tk.Label(window)
e.pack(); lbl.pack()
e.bind("<Return>", submit)

button_frame = tk.Frame(window)
nums = {i: f"Button{i}" for i in range(1, 10)}
ops = {' + ': 'plus', ' - ': 'minus', ' x ': 'multiply', ' / ': 'divide'}
for i in nums, ops:
    for el in i:
        globals()[i[el]] = tk.Button(button_frame, text = el, width = 5, command = lambda m = el: insert(m))

Button0 = tk.Button(button_frame, text = '0', width = 5, command = lambda m = '0': insert(m))
decimal = tk.Button(button_frame, text = '.', width = 5, command = lambda: e.delete(0, tk.END))
equal = tk.Button(button_frame, text = "=", width = 5, command = lambda m = '': submit(m))
Button0.grid(row = 3, column = 1); decimal.grid(row = 3, column = 2); equal.grid(row = 3, column = 3)

row, column = 0, 0
for i in nums:
    column += 1
    globals()[nums[i]].grid(row = row, column = column)
    if i % 3 == 0:
        row += 1; column = 0
row = -1
for i in ops:
    row += 1
    globals()[ops[i]].grid(row = row, column = 4)

def clear():
    e.delete(0, tk.END); lbl['text'] = ''
specials = tk.Frame(window)
b1, b2 = tk.Button(specials, width = 5), tk.Button(specials, width = 5)
clear = tk.Button(specials, width = 4, text = "C", font = "bold", command = clear)
clear.pack(side = 'left')
for i in b1, b2:
    i.pack(side = 'left')
def delete():
    op = [i for i in ops if e.get().endswith(i)]
    t = e.get().replace(op[0], '') if len(op) != 0 else e.get()[:len(e.get()) - 1]
    e.delete(0, tk.END); e.insert(0, t)
    if len(e.get()) == 0: lbl['text'] = ''
    
delete = tk.Button(specials, width = 5, text = "[x]", command = delete)
delete.pack(side = 'left')
specials.pack()
button_frame.pack()
window.bind("control-w", window.destroy)
