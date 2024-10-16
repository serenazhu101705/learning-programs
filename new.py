import tkinter as tk, os, string, module, random, time, lyricsModule
from tkinter.ttk import Combobox; from tkinter import messagebox, ttk; from PIL import Image

##this doesn't work, you need to fix it
class lyricsGame:
    window = tk.Tk()
    window.title("Lyrics Game Tkinter Version 2.0")
    ttk.Style().configure('TCombobox', relief='sunken', bd = 3)
    w, h = 750, 400; bg_color, fg_color = "white", "black"
    window.geometry("%sx%s" % (w, h))
    img_dir = "../lyrics game/album images/"; lyrics_dir = "../lyrics game/lyrics/"
    artists, one, titles, rbtns, needs, lines2, missed, words2 = [], [], [], {}, {}, [], {}, []
    def np_page(self, start2, start, end):
        global choices2
        for i in range(start2):
            self.rbtns[self.choices[i]]['button'].pack_forget()
        choices2 = [self.choices[i] for i in range(start, end)]
        for i, el in enumerate(sorted(choices2), start + 1):
            self.rbtns[el]['button']['text'] = "%s. %s" % (i, el)
            self.rbtns[el]['button']['width'] = max([len(i) for i in choices2])
            self.rbtns[el]['button'].pack()
        self.nb.place_forget(); self.random_btn.pack_forget(); self.random_btn = tk.Button(self.window, text = "Random Song", command = self.random_btni, bd = 3); self.random_btn.pack(side = 'bottom')
        self.pb.place(x = 250, y = 363)

    def prev_page(self):
        self.np_page(len(self.choices), 0 , 13); self.pb.place_forget(); self.nb.place(x = 460, y = 363); self.random_btn.pack_forget(); self.random_btn = tk.Button(self.frame2, text = "Random Song", command = self.random_btni, bd = 3); self.random_btn.pack(side = 'bottom')
    def random_btni(self):
        try: song = random.choice(self.choices)
        except: song = random.choice(list(self.rbtns))
        self.rbtns[song]['button'].invoke()
    
    def forget(self):
        for i in self.rbtns:
            try: self.rbtns[i]['button'].pack_forget()
            except: pass
        
    C = tk.Canvas(window)
    filename = tk.PhotoImage(master = tk.Canvas(window), file = "../lyrics game/my_logo.png")
    start_bg = tk.Label(window, image = filename, width = w, height = h, bg = bg_color)
    frame1 = tk.Label(window, bg = bg_color); frame2 = tk.Label(window, bg = bg_color)
    lbl = tk.Label(frame1, text = "Start typing below\nto search for a song", font = ("TkMenuFont", 10, "bold"), bg = bg_color, fg = fg_color)
    entry = tk.Entry(frame1, bd = 3, highlightcolor = bg_color)
    combo = Combobox(frame1, width = 5, height = 5)
    combo['values'] = ("Artist","Title"); combo.insert(0, "Title")
    random_btn = tk.Button(frame2, text = "Random Song", bd = 3)
    def make_some_btns(self):
        self.nb = tk.Button(self.window, text = "\N{RIGHTWARDS BLACK ARROW}", bd = 3, command = lambda: self.np_page(13, 13, len(self.choices)))
        self.pb = tk.Button(self.window, text = "\N{LEFTWARDS BLACK ARROW}", bd = 3, command = self.prev_page)
    def chosen(self):
        for i in self.frame1, self.frame2:
            i.pack_forget()
        self.start_bg.place_forget(); self.forget()
        for i in self.rbtns:
            if self.rbtns[i]['var'].get() != '':
                song = i
        for i in self.one:
            title = module.read(i, 'rl')[0].replace("\n","")
            image_name = self.img_dir + module.read(i, 'rl')[2].replace("\n","") + ".png"
            if title == song:
                with open(i) as fp:
                    for i , line in enumerate(fp):
                        if i > 3:
                            self.lines2.append(line)
                for i in range(len(self.lines2)):
                    self.needs[i] = []
                a = "".join(self.lines2)
                level_lbl = tk.Label(self.window, text = "Choose a level.")
                self.missingwords, self.levels = [], {}
                level_names = ["Beginner(7 random words)", "Intermediate (15 random words)","Advanced (30 random words)","Expert (Every word (Are you crazy?????))"]
                filename = tk.PhotoImage(master = tk.Canvas(window), file = image_name)
                background_label = tk.Label(window, image=filename, width = w, height = h)
                background_label.place(x = 0, y = 0)
                img = Image.open(image_name); w, h = img.size
                others = ['senorita', 'night changes', 'i should probably go to bed', 'just say you won\'t let go', 'life is good', 
                          'what a man gotta do', 'no stylist', 'mistletoe', 'love me less', 'knockin\' boots', 'in case you didn\'t know',
                          'echame la culpa', 'centerpoint road', 'boyfriend', 'blueberry faygo', 'chew on my heart', 'a thousand years',
                          'if i know me', 'vivir mi vida', 'love someone', 'rare', 'to die for', 'hollywood\'s bleeding', 'i\'m so tired',
                          's', 'j', 'lights down low', 'divinely uninspired', 'scorpion', 'like i\'m gonna lose you']
                bg_color = '#%02x%02x%02x' % filename.get(int(w/2), 0)
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
                    
    def make(self):
        for i in "country","rap","pop":
            l = os.listdir(self.lyrics_dir + i)
            self.one += [self.lyrics_dir + i + "/" + el for el in l]
        for i in self.one:
            title = module.read(i, 'rl')[0].replace("\n","")
            artist = module.read(i, 'rl')[1].replace("\n","")
            self.titles.append(title); self.artists.append(artist)            
        for i in self.titles:
            self.rbtns[i] = {}
            self.rbtns[i]['var'] = tk.StringVar()
            self.rbtns[i]['button'] = tk.Radiobutton(self.frame2, text = i, value = i, var = self.rbtns[i]['var'], highlightbackground = self.bg_color, bg = self.bg_color, fg = self.fg_color, font = ("Marjari", 10, "underline italic"), anchor = 'w', command = self.chosen)
    
    def search(self, event):
        good = False
        if self.combo.get() != "Artist" and self.combo.get() != "Title":
            self.combo.delete(0,tk.END);combo.insert(0, "Title")
        self.forget()
        j = self.entry.get()
        if event.char in string.printable and event.char not in ['\t', '\n', '\r', '\x0b', '\x0c']:
            j = self.entry.get() + event.char
        if event.char == "\x08" and len(j) >= 2:
            j = j[0 : len(j) - 1:].lower(); good = True
        self.choices = []
        for i in self.titles:
            if i.lower().startswith(j.lower()) and j != '' and self.combo.get() == "Title":
                self.choices.append(i)
        
        if self.combo.get() == "Artist" and j != '':
            for i in self.titles:
                words = i.split()
                for word in range(len(words)):
                    if "by" == words[word]:
                        start = word
                self.words2 = []
                for iel in range(start + 1, len(words)):
                    self.words2.append(words[iel])
                artist = " ".join(self.words2).lower()
                if artist.startswith(j.lower()):
                    self.choices.append(i); self.choices.sort()
                    
        try: m = max([len(i) for i in self.choices])
        except: m = 0
        if m <= 22: m = m + 5
        for i, el in enumerate(sorted(self.choices), 1):
            self.rbtns[el]['button']['text'] = "%s. %s" % (i, el)
            self.rbtns[el]['button']['width'] = m
            self.rbtns[el]['button'].pack()

        if len(self.choices) > 13 and len(j) != 0: self.nb.place(x = 460, y = 363)
        else: self.nb.place_forget()

        if event.char == '\x08' and not good and len(j) <= 1:
            self.choices = []; self.forget(); self.nb.place_forget(); self.pb.pack_forget()


    def start_game(self):
        self.start_bg.place(x = 0, y = 0)
        self.lbl.pack(); self.entry.pack(side = 'left')
        self.combo.pack(side = 'right')
        self.random_btn.pack(side = 'bottom')
        self.titles = list(set(self.titles))
        self.entry.bind("<Key>",self.search)
        self.combo.bind("<<ComboboxSelected>>", self.search)
    
        
game = lyricsGame()
game.make_some_btns()
game.start_game()
for i in game.frame1, game.frame2:
    i.pack()
game.make()
