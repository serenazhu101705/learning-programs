import tkinter as tk, string, pickle, os
from tkinter import messagebox

window = tk.Tk()
window.geometry("500x250")
window.resizable(width = False, height = False)
passed = False

def reset():
    users, passed, to = {}, False, None
    os.remove("save.dat")
    with open("save.dat", 'wb') as f:
        pickle.dump([users, passed, to], f, protocol = 2)

def check(event):
    global user
    if event.char == "\x08" and len(log.get()) <= 1:
        user = ''
    elif event.char == "\x08" and len(log.get()) > 1:
        user = log.get()[:-1]
    else:
        if event.char not in string.printable and event.char != '\x08' or event.char in ['\t', '\n', '\r', '\x0b', '\x0c']:
            user = log.get()
        else:
            user = log.get() + event.char
    t = "User found" if user in users else "User not found"
    t = "" if user == '' else t
    s = "normal" if user in users else "disabled"
    log_check.pack()
    log_check['text'] = t
    pw['state'] = s
    if event.char == '\t' and pw['state'] == "normal" or t == '': log_check.pack_forget()
    
def check_pass(event):
    global passed
    password = users[user]
    m = "Login Successful" if pw.get().lower() == password else "Login Unsuccessful"
    messagebox.showinfo(title = "Login", message = m)
    [i.delete(0, tk.END) for i in [log, pw]]
    log.focus_set()
    passed = True if m == "Login Successful" else False
    import date
    to = date.today
    with open("save.dat", 'wb') as f:
        pickle.dump([users, passed, to], f, protocol = 2)
    if m == "Login Successful": window.destroy()
    else: pw['state'] = 'disabled'; log_check['text'] = ''

def new_acc():
    frame1.pack_forget(); frame2.pack_forget(); frame3.pack();
    btn.place_forget(); new_user.focus_set()
    log.delete(0, tk.END); pw.delete(0, tk.END)

def sub():    
    users[new_user.get()] = new_pw.get()
    with open("save.dat","wb") as f:
        pickle.dump([users, passed, to], f, protocol = 2)
    messagebox.showinfo(title = "Account Created", message = "Account created")
    frame3.pack_forget(); frame1.pack(); frame2.pack(); btn.place(x = 166, y = 150)

def back():
    frame3.pack_forget(); frame1.pack(); frame2.pack()
    btn.place(x = 166, y = 150); log.focus_set()
    for i in new_user, new_pw, confirm:
        i.delete(0, tk.END)
    
def checked(event):
    if event.char == "\x08" and len(confirm.get()) <= 1:
        lbl6['text'] = ''
    if event.char == "\x08" and len(confirm.get()) <= len(new_pw.get()):
        submit['state'] = 'disabled'
    else:
        if event.char not in string.printable or event.char in ['\t', '\n', '\r', '\x0b', '\x0c']:
            pass
        else:
            if confirm.get() + event.char == new_pw.get():
                submit['state'] = 'normal'
                lbl6['text'] = ''
            else:
                lbl6['text'] = 'Passwords do not match.'

def checked2(event):
    if event.char == "\x08" and len(new_user.get()) <= 1:
        j = ''
    else:
        if event.char not in string.printable and event.char != '\x08' or event.char in ['\t', '\n', '\r', '\x0b', '\x0c']:
            j = new_user.get()
        else:
            if event.char == "\x08" and len(new_user.get()) > 1:
                j = new_user.get()[:-1]
            else:
                j = new_user.get() + event.char
    t = "" if j not in users else "User already in database."
    s = "normal" if j not in users else "disabled"
    lbl6['text'] = t
    confirm['state'], new_pw['state'] = s, s

for i in 'frame1', 'frame2', 'frame3':
    globals()[i] = tk.Frame(window)

lbl = tk.Label(frame1, text = "Login")
log = tk.Entry(frame1)
log_check = tk.Label(frame1)
lbl2 = tk.Label(frame2, text = "Password")
pw = tk.Entry(frame2, show = "*", state = "disabled")
btn = tk.Button(window, text = "Create New Account", command = new_acc)

new_user = tk.Entry(frame3)
new_pw, confirm = tk.Entry(frame3, show = "*", state = "disabled"), tk.Entry(frame3, show = "*", state = "disabled")
submit = tk.Button(frame3, text = 'Submit', command = sub, state = 'disabled')
back = tk.Button(frame3, text = "Back", command = back)

for i, el in {"lbl3": "Username", "lbl4": "Password", "lbl5": "Confirm Password", "lbl6": ''}.items():
    globals()[i] = tk.Label(frame3, text = el)

for i in lbl, log, lbl2, pw, lbl3, new_user, lbl4, new_pw, lbl5, confirm, lbl6, submit, back:
    i.pack()

frame1.pack(); frame2.pack()
btn.place(x = 166, y = 150); log.focus_set()

with open("save.dat","rb") as f:
    users, passed, to = pickle.load(f)

log.bind("<Key>", check); pw.bind("<Return>", check_pass)
pw.bind("<Button-1>", lambda event: log_check.pack_forget())
new_user.bind("<Key>", checked2); confirm.bind("<Key>", checked)

window.mainloop()
