import os, module, random, string

def choose(word, List, back = True):
    numbers = [str(i) for i in range(1, len(List) + 3)]
    print(f"\nChoose a {word}:\n")
    List.append(f"Random {word}")
    if back: List.append(f"Go back")
    for i, el in enumerate(List, 1): print(f"{i}. {el}\n")
    choice = input().lower()
    while choice not in [i.lower() for i in List] + numbers: print("Invalid. Please try again."); choice = input().lower()
    try: choice = List[int(choice) - 1]
    except: pass
    choice = random.choice(List[:len(List) - 2]) if "random" in choice.lower() else choice
    return choice

#game class
class hello:
    def __str__(self):
        print(f"{title}\n{artist}")
        for i in self.lyrics: print(i)
        print(f"\nYou have {len(self.missingwordslist)} words left")
        return ""
    def choose_genre(self):
        genres = [i.title() for i in os.listdir(directory)]
        self.genre = (choose("genre", genres, back = False) + "/").lower()
    def choose_song(self):
        self.directory2, titles, titles2, artists = directory + self.genre, [], [], []
        for i in os.listdir(self.directory2):
            lyrics = module.read(self.directory2 + i, 'rl')
            titles.append(lyrics[0].replace("\n",'')); artists.append(lyrics[1].replace("\n",''))
            artists = sorted(list(set(artists)))
        for i in artists:
            for el in titles:
                if i in el: titles2.append(el)
        self.song = choose("song", titles2)
    def choose_level(self):
        for i in os.listdir(self.directory2):
            self.lyrics = [i.strip() for i in module.read(self.directory2 + i, 'rl')]
            if self.lyrics[0] == self.song: self.highscore_file = highscores + i; break
        for i in 'title','artist','album': globals()[i] = self.lyrics.pop(0)
        self.keeps2, self.keeps, keeps, self.words, self.missingwordslist, self.keeps3 = [], [], [], ["'"], [], ["*", "'", "-"]
        self.sp = [i for i in self.lyrics if "-" in i]; self.specials = [i for i in string.punctuation if i not in self.keeps3]
        for i in self.sp: self.keeps += [el for el in i.split() if "-" in el]
        for i in self.keeps: self.keeps2 += i.split("-")
        self.lyrics2 = [i.replace("-", " ") for i in self.lyrics]
        for i in self.lyrics2: self.words += i.split()
        self.cakes = [i for i in self.words if i.endswith("in'")]
        module.Replace(self.words, keeps); module.Replace(self.words, string.punctuation)
        self.words = list(set([i.lower() for i in self.words if i != '']))
        self.levels = {"Beginner": 7, "Intermediate": 15, "Advanced": 30, "Expert": len(self.words)}
        try: self.level = self.levels[choose("level", list(self.levels))]
        except: self.level = 'Go back'
    def replace_words(self):
        while len(self.missingwordslist) < int(self.level):
            self.missingwordslist.append(random.choice(self.words))
            self.missingwordslist = list(set(self.missingwordslist))        
        for i in range(len(self.lyrics)):
            k = self.lyrics[i].split(); module.Replace(k, self.specials)
            for iel in range(len(k)):
                raw = module.Replace2([i for i in string.punctuation if i != "*"], k[iel]).lower()
                if raw in self.missingwordslist:
                    k2 = [i.lower() for i in k]; module.Replace(k2, string.punctuation)
                    k[iel] = k2[iel].replace(raw, "_" * len(k[iel]))
            self.lyrics[i] = " ".join(k)
            for haha in self.keeps2:
                if haha in self.missingwordslist:
                    self.lyrics[i] = self.lyrics[i].replace(haha, "_" * len(haha))
        self.missingwordslist = [i for i in self.missingwordslist if i not in self.cakes]
        self.missingwordslist += [i.replace("in'", "ing") for i in self.cakes]
    def start_game(self):
        self.clue, self.wrong, self.hacked = 0, 0, False
        self.answerslist = set()
        while len(self.missingwordslist) != 0:
            answer = (module.Replace2(string.punctuation, input().lower()))
            answer = answer.replace("in", "ing") if answer.replace("in", "ing") in self.missingwordslist + list(self.answerslist) else answer
            if answer in self.missingwordslist:
                self.missingwordslist.remove(answer); self.answerslist.add(answer)
                status = f"{len(self.missingwordslist)} words left." if len(self.missingwordslist) != 0 else "now finished the game!\n"
                print(f"Correct! You have now {status}")
            elif answer in self.answerslist: print(f"You've already guessed this word. You have {len(self.missingwordslist)} words left")
            elif answer == "give up":
                print("Here are the rest of the words:\n")
                for i in self.missingwordslist: print(u'\u2022' + str.capitalize(i))
                break
            elif answer == 'serenaisawesome':
                see = input("Welcome Master Serena! What would you like to see?\n")
                if see == 'nothing': self.hacked = True; self.missingwordslist.clear()
                if self.level != len(self.words):
                    for i in self.missingwordslist: print(u'\u2022' + str.capitalize(i))
                else: print(self.missingwordslist)
            elif answer == 'clue':
                if self.clue < 3:
                    print(f"Clue: {random.choice(self.missingwordslist)}\nYou have {2 - clue} clues left.")
                    self.clue = self.clue + 1
                else: print("Sorry. You are out of clues.")
            else:
                print("Incorrect. Please try again."); self.wrong = self.wrong + 1
                if self.wrong >= 8: print("Give up? End the game by typing 'Give up'")
                if self.clue < 3: print("Type 'clue' below to get a word")

    def score(self):
        scores = module.read(self.highscore_file, 'rl')
        for i in scores:
            if str(self.level) in i:
                high_score = i.split(":")[1].strip()
                strlevel = [i for i in self.levels if self.levels[i] == self.level][0]
                break
        if self.level == len(self.words):
            strlevel = "Expert"; high_score = scores[len(scores) - 1].split(":")[1].strip()
        print(f"The high score for the {strlevel.lower()} level of this song is {high_score}")
        score = (len(self.answerslist)/(self.level + self.wrong)) * 100 
        score = round(score - ((1/3) * self.clue), 1) if not self.hacked else 100.0
        print(f"Your score for this level is {score}")
        if score >= float(high_score):
            status = "set a new" if score > float(high_score) else "tied the"
            print(f"Congrats! You just {status} high score for this level!\n")
            l = i.split(":"); l[1] = l[1].replace(high_score, str(score))
            for el in range(len(scores)):
                if strlevel in scores[el]:
                    scores[el] = ":".join(l)
                    break
            reset = module.yesorno("Would you like to reset your high scores?")
            if reset == 'yes':
                r = input("Reset level, song, or game?\n"); self.hacked = False
                if r == 'level': n = scores[el].split(":"); n[1] = " 0\n"; scores[el] = ":".join(n)
                if r == 'song': scores = ['Beginner(7 random words): 0\n', 'Intermediate (15 random words): 0\n', 'Advanced (30 randomwords): 0\n', 'Expert (Every word (Are you crazy?????)): 0']
                if r == 'game':
                    pw = input('please enter the password to authorize access: '); tries = 1
                    while pw != 'iluvserenazhu' and tries < 5:
                        pw = input("access denied. "); tries = tries + 1
                        if tries == 5: print('killing session'); exit()
                    for i in os.listdir(highscores):
                        with open(highscores + i, 'w') as f:
                            f.write('Beginner(7 random words): 0\nIntermediate (15 random words): 0\nAdvanced (30 randomwords): 0\nExpert (Every word (Are you crazy?????)): 0')
            if not self.hacked:                
                with open(self.highscore_file, 'w') as file:
                    file.write("".join(scores))
    
#start game
game = hello(); play = "yes"
while play == 'yes':
    #important directories
    directory, highscores = '../lyrics game/lyrics/', '../lyrics game/high scores/'

    #run loop to choose song, level, and genre
    step = -1; steps = [game.choose_genre, game.choose_song, game.choose_level]
    while step < 2:
        step = step + 1; steps[step]()
        if step != 0:
            try: step = step - 2 if game.song == 'Go back' else step
            except: pass
            try: step = step - 2 if game.level == 'Go back' else step
            except: pass
    game.replace_words()

    #start and score game
    print(game); game.start_game(); game.score()
    play = module.yesorno("\nWould you like to play again?")
    
feedback = module.yesorno("Would you like to leave feedback?")
if feedback == 'yes':
    feedback = input("\nType your feedback below:\n")
    with open('../lyrics game/feedback', 'a') as file:
        file.write(f"\n\n\u2022 {feedback}")
print("Thanks for playing!")
