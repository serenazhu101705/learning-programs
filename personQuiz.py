import tkinter as tk
window = tk.Tk()
window.geometry("500x400")
frame1 = tk.Frame(window); frame2 = tk.Frame(window)
frame1.pack(); frame2.pack()
lbl = tk.Label(frame1, text = 'Would Serena Zhu Date You? Press the START button to find out!')
number = -1
questions = {'What is your most admirable trait?': {'Funny and Outgoing' : 9, 'Quiet and Shy' : 5, 'Loud and Obnoxious' : 4, 'Cool and Confident' : 8, 'Kind and Generous' : 9, 'Thoughtful and Loving' : 9, 'Smart and Reasonable' : 5, 'Athletic and Strong' : 9},
             'How athletic are you?': {"Very athletic, I play a ton of sports and I'm amazing." : 10, "Decently, I play a few sports and I'm pretty good." : 9, 'Average, I play one sport and I am okay.' : 7, "Below average, I don't play any sports, but I have an A in gym" : 4, 'I suck.' : 3},
             'What color is your natural hair?': {'Black' : 6, 'Brown' : 8, 'Platnium blond' : 8, 'Dirty blond' : 9, 'Regular blond' : 10, 'Red' : 7},
             'What color are your eyes?': {'Dark brown' : 8, 'Brown' : 7, 'Pale blue' : 9, 'Blue' : 9, 'Gold' : 8, 'Hazel' : 8, 'Green' : 8, 'I have two different colored eyes' : 8},
             'Are you fat?': {'I am obese' : 1, 'I am overweight' : 3, 'I am a little chubby, but not fat.' : 4, 'I am average' : 7, "I'm ripped" : 9, "I'm Zac Efron" : 10},
             'Rate yourself on a scale of 1 - 5': {'1' : 4, '2' : 6, '3' : 9, '4' : 7, '5' : 5},
             'How tall are you?': {'6 ft or above' : 9, '5 ft 9 to 5 ft 11' : 9, '5 ft 4 to 5ft 8' : 6, '5 ft to 5 ft 3' : 3, 'Below 5 ft' : 1}}

def final():
    chosen = []; score = 0
    for i in rbtns:
        if rbtns[i]['var'].get() != '':
            chosen.append(rbtns[i]['button']['text'])
    for i in range(len(chosen)):
        q = list(questions)[i]
        c = questions[q][chosen[i]]
        score = score + c
    for i in rbtns:
        rbtns[i]['button'].pack_forget()
    lbl['text'] = 'Your score is %s' % score; next_btn['command'] = window.destroy
def check2(event):
    global number
    for i in rbtns:
        if rbtns[i]['var'].get() != '':
            for i in questions[list(questions)[number]]:
                if rbtns[i]['var'].get() != '' :
                    rbtns[i]['var'].set('')
    next_btn['state'] = 'normal'
            
rbtns = {}
for i, el in questions.items():
    for i in el:
        rbtns[i] = {}
        rbtns[i]['var'] = tk.StringVar()
        rbtns[i]['button'] = tk.Radiobutton(frame2, text = i, value = i, var = rbtns[i]['var'], anchor = 'w')
        rbtns[i]['button'].bind("<Button-1>", check2)


def new():
    global number, rbtns
    next_btn['state'] = 'disabled'
    for i in rbtns:
            rbtns[i]['button'].pack_forget()
    for i in questions[list(questions)[number]]:
        rbtns[i]['button'].pack(side = 'top', anchor = 'w')
    for i in questions[list(questions)[number]]:
        if rbtns[i]['var'].get() != '':
            next_btn['state'] = 'normal'

def move(direction):
    global number, rbtns
    if direction == "next":
        number = number + 1
        if number == len(questions) - 1:
            next_btn['text'] = 'FINISH'; next_btn['command'] = final
    else:
        number = number - 1; button = next_btn
        if number == 0:
            prev_btn['state'] = 'disabled'
    lbl['text'] = list(questions)[number]; new()
    
def Next(): move('next'); prev_btn['state'] = 'normal'
def Previous(): move('prev')

def Start():
    Next(); start.pack_forget(); prev_btn['state'] = 'disabled'
    prev_btn.pack(side = 'left'); next_btn.pack(side = 'right')

next_btn = tk.Button(window, text = "NEXT", bd = 3, command = Next)
prev_btn = tk.Button(window, text = "PREVIOUS", bd = 3, command = Previous)
start = tk.Button(window, text = "START", bd = 3, command = Start)

lbl.pack(side = 'top'); start.pack(side = 'top')
