import tkinter as tk, os, string, module, random, time, lyricsModule
from tkinter.ttk import Combobox; from tkinter import messagebox, ttk; from PIL import Image

window = tk.Tk()
window.title("Lyrics Game Tkinter Version 1.0")
ttk.Style().configure('TCombobox', relief='sunken', bd = 3)
w, h = 750, 400
window.geometry("%sx%s" % (w, h))
directory1 = "../lyrics game/album images/"
directory = '../lyrics game/lyrics/'
artists, one, titles, rbtns, needs, lines2, missed = [], [], [], {}, {}, [], {}

def np_page(start2, start, end):
    global choices, choices2, rbtns, pb, random_btn
    for i in range(start2):
        rbtns[choices[i]]['button'].pack_forget()
    choices2 = [choices[i] for i in range(start, end)]
    for i, el in enumerate(sorted(choices2), start + 1):
        rbtns[el]['button']['text'] = "%s. %s" % (i, el)
        rbtns[el]['button']['width'] = max([len(i) for i in choices2])
        rbtns[el]['button'].pack()
    nb.place_forget(); random_btn.pack_forget(); random_btn = tk.Button(window, text = "Random Song", font = font_choice, command = random_btni, bd = 3); random_btn.pack(side = 'bottom')
    pb.place(x = 250, y = 363)
    

def next_page():
    np_page(13, 13, len(choices))

def prev_page():
    global random_btn
    np_page(len(choices), 0 , 13); pb.place_forget(); nb.place(x = 460, y = 363); random_btn.pack_forget(); random_btn = tk.Button(frame2, text = "Random Song", font = font_choice, command = random_btni, bd = 3); random_btn.pack(side = 'bottom')

def random_btni():
    try: song = random.choice(choices)
    except: song = random.choice(list(rbtns))
    rbtns[song]['button'].invoke()

def forget():
    global rbtns
    for i in rbtns:
        try: rbtns[i]['button'].pack_forget()
        except: pass
        
def search(event):
    global words2, choices, next_page, nb, pb, prev_page, np_page
    good = False
    if combo.get() != "Artist" and combo.get() != "Title":
        combo.delete(0,tk.END);combo.insert(0, "Title")
    forget()
    j = entry.get()
    if event.char in string.printable and event.char not in ['\t', '\n', '\r', '\x0b', '\x0c']:
        j = entry.get() + event.char
    if event.char == "\x08" and len(j) >= 2:
        j = j[0 : len(j) - 1:].lower(); good = True
    choices = []
    for i in titles:
        if i.lower().startswith(j.lower()) and j != '' and combo.get() == "Title":
            choices.append(i)
    
    if combo.get() == "Artist" and j != '':
        for i in titles:
            words = i.split()
            for word in range(len(words)):
                if "by" == words[word]:
                    start = word
            words2 = []
            for iel in range(start + 1, len(words)):
                words2.append(words[iel])
            artist = " ".join(words2).lower()
            if artist.startswith(j.lower()):
                choices.append(i); choices.sort()
                
    try: m = max([len(i) for i in choices])
    except: m = 0
    if m <= 22: m = m + 5
    for i, el in enumerate(sorted(choices), 1):
        rbtns[el]['button']['text'] = "%s. %s" % (i, el)
        rbtns[el]['button']['width'] = m
        rbtns[el]['button'].pack()

    if len(choices) > 13 and len(j) != 0: nb.place(x = 460, y = 363)
    else: nb.place_forget()

    if event.char == '\x08' and not good and len(j) <= 1:
        choices = []
        forget(); nb.place_forget(); pb.pack_forget()
      
def chosen():
    global lines, selected, linesdict, missingwords, lines2, missed, song, level_names, levels, a, intro_lbl, needs, image, bg_color, fg_color, C, image_name, filename, background_label, img, blacks, w,h
    for i in entry, combo, frame1, frame2:
        i.pack_forget()
    start_bg.place_forget(); forget()
    for i in rbtns:
        if rbtns[i]['var'].get() != '':
            song = i
    for i in one:
        title = module.read(i, 'rl')[0].strip()
        image_name = directory1 + module.read(i, 'rl')[2].strip() + ".png"
        if title == song:
            with open(i) as fp:
                for i , line in enumerate(fp):
                    if i > 3:
                        lines2.append(line)
            for i in range(len(lines2)):
                needs[i] = []
            a = "".join(lines2)
            level_lbl = tk.Label(window, text = "Choose a level.")
            missingwords, levels = [], {}
            level_names = ["Beginner(7 random words)", "Intermediate (15 random words)","Advanced (30 random words)","Expert (Every word (Are you crazy?????))"]
            filename = tk.PhotoImage(master = C, file = image_name)
            background_label = tk.Label(window, image=filename, width = w, height = h)
            background_label.place(x = 0, y = 0)
            img = Image.open(image_name); w2, h2 = img.size
            others = ['senorita', 'night changes', 'i should probably go to bed', 'just say you won\'t let go', 'life is good', 
                      'what a man gotta do', 'no stylist', 'mistletoe', 'love me less', 'knockin\' boots', 'in case you didn\'t know',
                      'echame la culpa', 'centerpoint road', 'boyfriend', 'blueberry faygo', 'chew on my heart', 'a thousand years',
                      'if i know me', 'vivir mi vida', 'love someone', 'rare', 'to die for', 'hollywood\'s bleeding', 'i\'m so tired',
                      's', 'j', 'lights down low', 'divinely uninspired', 'scorpion', 'like i\'m gonna lose you']
            bg_color = '#%02x%02x%02x' % filename.get(int(w2/2), 0)
            if image_name in ["../lyrics game/album images/" + i + '.png' for i in others]:
                bg_color = lyricsModule.compute_average_image_color(img)
            blacks = ["fine line", 'shawn mendes', 'scorpion', 'comethru', 'from the ground up', 'locked away', 'all to myself',
                      'i should probably go to bed', 'popstar', 'tangled up', 'going bad', 'handwritten', 'senorita', 'if the world was ending',
                      'if i know me', 'love someone', 'rare', 'hollywood\'s bleeding', 'i\'m so tired', 'divinely uninspired', 'they don\'t know about us',
                      'no stylist', 'night changes', 'mistletoe', 'knockin\' boots', 'kiss you', 'dangerous woman', 'in case you didn\'t know', 'echame la culpa',
                      'easier', 'who do you love', 'what a man gotta do', 'paradise', 'centerpoint road', 'chew on my heart', 'a thousand years', 'toosie slide',
                      'consequences', 'never be the same', 'z', '26', 's', 'j', 'lights down low', 'i don\'t wanna live forever']
            if image_name in ["../lyrics game/album images/" + i + '.png' for i in blacks]:
                fg_color = "white"
            else:
                fg_color = "black"

            window.config(bg = bg_color); background_label['bg'] = bg_color
            intro_lbl = tk.Label(window, text = "Fill in the missing lyrics for %s.\n" % song, bg = bg_color, fg = fg_color, highlightbackground = bg_color, font = ("Marjari",10,"bold underline"), highlightthickness = 5); intro_lbl.pack(side = "top")
            for i in level_names:
                levels[i] = {}
                levels[i]['var'] = tk.StringVar()
                levels[i]['button'] = tk.Radiobutton(window, text = i, value = i, var = levels[i]['var'], command = level_chosen, font = ("Marjari", 10, "underline italic"), relief = 'raised', bd = 5, width = 35, anchor = 'w', highlightbackground = bg_color)
                levels[i]['button']['highlightthickness'] = 3
            for i in levels:
                levels[i]['button'].pack()
            break

def start_game():
    global C, filename, start_bg, frame1, frame2, bg_color, fg_color, font_choice, lbl, entry, combo, rbtns, one, choices, titles, artists, titles, needs, random_btn, nb, pb
    bg_color = "white"; fg_color = "black"; font_choice = "TkMenuFont"
    C = tk.Canvas(window)
    filename = tk.PhotoImage(master = C, file = "../lyrics game/my_logo.png")
    start_bg = tk.Label(window, image=filename, width = w, height = h, bg = bg_color)
    start_bg.place(x = 0, y = 0)
    frame1 = tk.Frame(window, bg = bg_color); frame2 = tk.Frame(window, bg = bg_color)
    np_frame = tk.Frame(window, bg = bg_color); np_frame.pack(side = 'bottom')
    lbl = tk.Label(frame1, text = "Start typing below\nto search for a song", font = (font_choice, 10, "bold"), bg = bg_color, fg = fg_color)
    entry = tk.Entry(frame1, bd = 3, highlightcolor = '#d9d9d9'); lbl.pack(); entry.pack(side = 'left')
    combo = Combobox(frame1, width = 5, height = 5, font = font_choice)
    combo['values'] = ("Artist","Title")
    combo.insert(0, "Title"); combo.pack(side = 'right')
    random_btn = tk.Button(frame2, text = "Random Song", font = font_choice, command = random_btni, bd = 3); random_btn.pack(side = 'bottom')
    artists, one, titles, rbtns, needs, lines2, missed = [], [], [], {}, {}, [], {}    
    nb = tk.Button(window, text = "\N{RIGHTWARDS BLACK ARROW}", command= next_page, font = font_choice, bd = 3)
    pb = tk.Button(window, text = "\N{LEFTWARDS BLACK ARROW}", command = prev_page, font = font_choice, bd = 3)
    for i in "country","rap","pop":
        l = os.listdir(directory + i)
        one += [directory + i + "/" + el for el in l]
    for i in one:
        title = module.read(i, 'rl')[0].strip()
        artist = module.read(i, 'rl')[1].strip()
        titles.append(title); artists.append(artist)
    for i in titles:
        rbtns[i] = {}
        rbtns[i]['var'] = tk.StringVar()
        rbtns[i]['button'] = tk.Radiobutton(frame2, command = chosen, text = i, value = i, var = rbtns[i]['var'], highlightbackground = bg_color, bg = bg_color, fg = fg_color, font = ("Marjari", 10, "underline italic"), anchor = 'w')
    frame1.pack(); frame2.pack()
    titles = list(set(titles))
    entry.bind("<Key>",search)
    combo.bind("<<ComboboxSelected>>", search)

start_game()
        
def np():
    global l, words, needs, missed, level_choice, fullline, newline, start, end
    coi_lbl.pack(); clue_btn.pack(side = "left"); help_btn.pack(side = "right"); clue_lbl.pack(side = "bottom")
    coi_lbl['text'] = ''
    m_lbl['state'] = 'normal'
    m_lbl.delete('1.0',tk.END)
    m_lbl.insert("1.0", newline)
    m_lbl['state'] = 'disabled'
    mylist.select_clear(start)
    mylist.select_set(end)
    clue_lbl['text'] = ''
    l = list(mylist.curselection())[0]
    mylist.see(l)
    if l == 0:
        prev_btn['state'] = 'disabled'
    else:
        good = False
        for i in range(len(list(mylist.get(0,tk.END)))):
            if "_" in list(mylist.get(0,tk.END))[i] and i < l:
                good = True
        if not good:
            prev_btn['state'] = 'disabled'
        else:
            prev_btn['state'] = 'normal'
    words = []
    k = needs[l]
    for i in missed:
        if "Expert" in level_choice:
            if fullline.replace("\n","") == i:
                words += i.split(); words = lyricsModule.create(words); module.remove(words, "")
                break
        else:
            if fullline in missed[i] and "_" in newline and i not in k:
                    words.append(i)
    if len(words) != 0:
            for i in m_entry, clue_btn:
                i['state'] = 'normal'
    else:
            for i in m_entry, clue_btn:
                i['state'] = 'disabled'

def next():
    global start, fullline, newline, l, end
    lines3 = list(mylist.get(0, tk.END))
    current = m_lbl.get('1.0',tk.END).replace("\n","")
    start = list(mylist.curselection())[0]
    for i in range(len(lines3)):
        if "_" in lines3[i] and i > start:
            newline = lines3[i]
            fullline = lines2[i]
            end = i
            break
    np()

def previous():
    global start, fullline, newline, l, end
    lines3 = list(mylist.get(0, tk.END))
    current = m_lbl.get('1.0',tk.END).replace("\n","")
    start = list(mylist.curselection())[0]
    for i in range(len(lines3)):
        if "_" in lines3[i] and i < start:
            newline = lines[i]
            fullline = lines2[i]
            end = i
    np()

def selected(event):
    global fullline, end, newline, start
    start = mylist.curselection()[0]
    fullline, newline, end = lines2[start], lines[start], start
    np()
    

def clue():
    if len(words) != 0:
        clue_lbl.pack()
        clue_lbl['text'] = "Here's a clue:\n%s" % random.choice(words)
    else:
        clue_lbl['text'] = ''

def give_up():
    global l, start, level, level_choice, start_game
    play = messagebox.askyesno(title = "Play again?", message = "Thanks for playing! Do you want to play again?")
    if play:
        entry.delete(0, tk.END)
        m_entry.delete(0, tk.END)
        m_lbl['state'] = 'normal'
        m_lbl.delete("1.0",tk.END)
        m_lbl['state'] = 'disabled'
        for i in end_forgets:
            i.pack_forget()
        
        mylist.delete(0,tk.END)
        background_label.place_forget()
        start_game()
        frame1['bg'] = bg_color; frame2['bg'] = bg_color; lbl['bg'] = bg_color; lbl['fg'] = fg_color
        for i in rbtns:
            rbtns[i]['button']['bg'] = bg_color
            rbtns[i]['button']['fg'] = fg_color
            rbtns[i]['button']['highlightbackground'] = bg_color
            if image_name in ["../lyrics game/album images/" + i + '.png' for i in blacks]:
                rbtns[i]['button']['highlightcolor'] = 'white'
            else:
                rbtns[i]['button']['highlightcolor'] = 'black'
        lbl['text'] = "Start typing below\nto search for a song"; clue_lbl['text'] = ''
        entry.pack(side = 'left'); combo.pack(side = 'right'); rbtns[song]['var'].set(""); clue_lbl['text'] = ''
        if "level" in globals():
            del level
        try: del l
        except: pass
        try: del start
        except: pass
        
    else:
        window.destroy()

def enter(event):
    global words, word, res, reslist, l, start, level, level_choice
    res = m_entry.get();m_entry.delete(0,tk.END); clue_lbl['text'] = ''
    k = needs[l]
    if res.lower() in [i.lower() for i in words] and res.lower() not in [i.lower() for i in k]:
        coi_lbl['text'] = "Good Job!"
        for i in words:
            if res.lower() == i.lower():
                word = i
        res = m_lbl.get('1.0',tk.END); reslist = res.split(); reslist2 = lines2[l].replace("\n","").split();reslist3 = [i.replace(word.lower(),"_" * len(word)).replace(str.capitalize(word), "_" * len(word)) for i in reslist2]
        for i in range(len(reslist)):
            test = reslist2[i].replace(str.capitalize(word), "_" * len(word))
            test1 = test.replace(word.lower(), "_" * len(word))
            if test1 == reslist3[i]:
                words2 = [i for i in words if i != word.lower() and i != str.capitalize(word) and i not in needs[l]]; reslist4 = [i for i in reslist2]
                for number in range(len(reslist2)):
                    for iel in words2:
                        if iel in reslist2[number]:
                            reslist4[number] = reslist2[number].replace(iel, "_" * len(iel))
                reslist[i] = reslist4[i]
                    
        res = " ".join(reslist)
        m_lbl['state'] = 'normal'; m_lbl.delete('1.0', tk.END); m_lbl.insert('1.0', res); m_lbl['state'] = 'disabled'
        lines[l] = res
        mylist.delete(l)
        mylist.insert(l,res)
        words = [i for i in words if i.lower() != word.lower()]
        if "Expert" not in level_choice:
            missed[word].remove(lines2[l])
        needs[l].append(word)
        mylist.select_set(l)
        if len(words) == 0:
            if "Expert" in level_choice:
                for i in range(len(missed)):
                    if missed[i] == fullline.replace("\n",""):
                        missed.pop(i)
                        break
            for i in clue_btn, m_entry:
                i['state'] = 'disabled'
            clue_lbl['text'] = ''
        if list(mylist.get(0,tk.END)) == [i.replace("\n","") for i in lines2]:
            give_up()
    else:
        coi_lbl['text'] = "Incorrect. Try again."
    
def level_chosen():
    global mylist, scrollbar, scrollbar2, missingwords, lines, a, level, removes, end_forgets, level_choice, missed, removes, frame3, frame4, frame5, frame6, next_btn, help_btn, m_lbl, m_entry, clue_lbl, coi_lbl, prev_btn, clue_btn, entry, lbl, give_up, end_forgets, newline, fullline, end, start
    removes = set()
    for i in levels:
        levels[i]['button'].pack_forget()
        if levels[i]['var'].get() != '':
            level_choice = i
    for i in '7','15','30':
        if i in level_choice:
            level = int(i)
            break
    
    if "level" in globals():
        while len(missingwords) != level:
            removes, adds = set(), set()
            while len(missingwords) != level:
                if len(missingwords) > level:
                    missingwords.pop(random.randint(0,len(missingwords)))
                else:
                    missingwords.append(random.choice(" ".join(lines2).split()))
            for i in missingwords:
                for el in missingwords:
                    if i in el and i != el:
                        removes.add(i)
            missingwords = [i for i in missingwords if i != 'a' and i != '']
            missingwords = lyricsModule.create(missingwords)
            for i in missingwords:
                for el in missingwords:
                    if i.lower() == el and i != el:
                        missingwords.remove(i)
            missingwords = [i for i in missingwords if i not in removes]
            missed = {}
        for i in missingwords:
            a = a.replace(i, "_" * len(i))
            missed[i] = []
        for i in missingwords:
            for el in lines2:
                if i in el:
                    missed[i].append(el)

        lines = a.splitlines()
    
    else:
        missingwords = [i for i in " ".join(lines2).split() if i != '']
        missingwords = lyricsModule.create(missingwords)
        module.remove(missingwords, "a", '')
        lines = a.splitlines()
        for i in range(len(lines)):
            for el in lines[i]:
                if el in string.ascii_letters or el in string.digits or el == "'":
                    lines[i] = lines[i].replace(el, "_")
        for i in missingwords:
            for el in missingwords:
                if i in el and i != el:
                    removes.add(i)
        missingwords = [i for i in missingwords if i not in removes]
        missed = a.splitlines()
        
    for i in range(len(lines2)):
        for el in lines2[i].split():
            if el.endswith("in'"):
                l = lines2[i]
                lines2[i] = lines2[i].replace(el, el.replace("in'","ing")); c = lines2[i]
                if "Expert" in level_choice:
                    missed[i] = lines2[i].replace("\n","")
                else:
                    for ha in missed:
                        for haha in range(len(missed[ha])):
                            if missed[ha][haha] == l:
                                missed[ha][haha] = c
                
    frame4 = tk.Frame(window, bg = bg_color); frame5 = tk.Frame(window, bg = bg_color); frame6 = tk.Frame(frame5, bg = bg_color);frame3 = tk.Frame(frame5, bg = bg_color)
    scrollbar = tk.Scrollbar(frame3, relief = 'groove', bd = 3)
    mylist = tk.Listbox(frame3, width = 40, highlightbackground = 'black', highlightthickness = 5, relief = 'ridge', bd = 10); m_entry = tk.Entry(frame4, state = 'disabled')
    m_lbl = tk.Text(frame4, state = "disabled", bd = 5, width = 40, height = 2, highlightthickness = 3, highlightbackground = 'black', highlightcolor = 'black'); coi_lbl = tk.Label(frame4, bg = bg_color, fg = fg_color); clue_lbl = tk.Label(frame4, bg = bg_color, fg = fg_color)
    scrollbar2 = tk.Scrollbar(frame3, orient = "horizontal", relief = 'groove', bd = 3)
    next_btn = tk.Button(frame6, text = '  Next  ', command = next, bd = 3)
    clue_btn = tk.Button(frame4, text = "Clue", command = clue, bd = 3); help_btn = tk.Button(frame4, text = "Give Up", command = give_up, bd = 3)
    prev_btn = tk.Button(frame6, text = "Previous", command = previous, state = 'disabled', bd = 3)
    mylist.bind("<Double-Button-1>",selected)
    m_entry.bind("<Return>", enter)
    for i in lines:
        mylist.insert("end",i)
    
    frame5.pack(side = "left"); frame6.pack(side = 'bottom'); frame3.pack(side = 'bottom'); frame4.pack(side = "right")
    scrollbar.config(command = mylist.yview); scrollbar2.config(command = mylist.xview)
    scrollbar.pack(side = 'right', fill = 'y'); scrollbar2.pack(side = "bottom", fill = "x"); prev_btn.grid(row = 0, column = 0)
    mylist['yscrollcommand'] = scrollbar.set; mylist['xscrollcommand'] = scrollbar2.set                    
    mylist.pack(side = "left", fill = "both"); m_lbl.pack(); m_entry.pack();next_btn.grid(row = 0, column = 1)
    end_forgets = [frame5, frame3, intro_lbl, frame4]
    newline, fullline, end, start = lines[0], lines2[0], 0, 0
    np(); mylist.yview_scroll(-1, 'units')
