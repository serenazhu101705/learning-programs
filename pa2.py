import webbrowser, subprocess, random, pickle, string, module, os, calendar, date as d, time as t

today = d.today
with open("save.dat", "rb") as f:
    users, passed, to = pickle.load(f)

if str(to) == str(today): passed = True
else: exec(open("./login.py").read())

reset = lambda: os.remove("savefile.dat")

def database():
    with open("savefile.dat","wb") as f:
        pickle.dump([name, player, built_in],f, protocol = 2)
        
new = False
try:
    with open("savefile.dat","rb") as f:
        name, player, built_in = pickle.load(f)
except: new = True

directory = '../personal assistant/'

#GET READY FOR HARRY!!!
if passed:
    if new:
        exec(open("./tutorial.py").read())
        name = input("Welcome! This is your personal assistant. What would you like to name me?\n").lower()
        idks = ['idk', 'i don\'t know', 'i dont know', '']
        print(f"\nMy name is now {string.capwords(name)}!") if name not in idks else print("Harry is my built-in name. You may call me Harry.")
        name = string.capwords(name) if name not in idks else "Harry"
        built_in = True if name == "Harry" else False
            
        print("What would you like me to call you?")
        player = string.capwords(input())
        while player == '':
            print("Sorry, you must input a name."); player = string.capwords(input())
        print("Hey we have the same name!") if name == player else None

        bosses = ["serena zhu","serena","serena rui","serena rui zhu","your boss","your master","your manufacturer","the awesomest","the coolest"]
        if player.lower() in bosses:
            boss = module.yesorno("Would you like me to call you Boss Master Serena?")
            player = "Boss Master Serena" if boss == "yes" else player
        print(f"\nHi there, {player}!")
        database()
        
    else: print(f"Welcome back, {player}!")

    exec(open(f"{directory}holidays.py").read())
    print(f"""\nWhat do you want to talk about?\n
For a list of things you can talk about with me, just type in:
{name}, what can we talk about?\"""")


    #specials
    holidays2 = [holidays[i][0] for i in holidays if type(holidays[i][0]) == str]
    specials = [holidays[i] for i in holidays if type(holidays[i][0]) == list]
    ks = []
    for i in specials:
        for el in range(len(i)):
            ks.append(i[el][0])
    holidays2 += ks

    asdf = {1: "st", 2: "nd", 3: "rd"}
    ordinal = lambda n: f"{n}{asdf[n % 10]}" if n % 10 in asdf and n // 10 % 10 != 1 else f"{n}th"
    dates = []
    month_days = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6:30, 7: 31, 8: 31, 9: 30, 10:31, 11: 30, 12: 31}
    for i, el in month_days.items():
        for iel in range(1, el + 1):
            dates.append(f"{list(calendar.month_name)[i]} {iel}")
    
    #choices
    talks = {'date2': ['what time is it',"what's the date"] + ["what day of the week is " + i for i in dates] + ['how many days until ' + i for i in dates],
             'joke':["tell me a joke."], 'game': ["play a game."],
             'file': ["open a file.", "delete a file."], 'tutorial': ["open the tutorial."],
             'holidays': [f"when is {i}" for i in holidays2],
             'reviews': ["show me some reviews about yourself.", 'leave some feedback.'],
             'contact': ["check my contacts."],
             'website': ['google something.', 'open a website.', 'check MyCircle.', "google an image."],
             'ask':["what's your name", "what's my name","what can we talk about",
              "change your name.", "change my name.",
              "who am I","who are you"]}

    #replaces
    goodbyes = ["bye", "goodbye", "adios", "see you later", 'nothing', 'bye bye']
    idks = ['idk', 'i dont know', 'im bored', '']
    hellos = ['hi', 'hey', 'hello', 'hola', 'aloha', 'wassup', 'sup']
    harry = [f"I'm here, {player}.", "Right here, at your service", "I'm listening."]
    not_goods = [f"{name.lower()} ", f" {name.lower()}", f"{name.lower()}", 'can i ', 'can you ']

    again = True
    
    while again:
        ask = input().lower()
        j = [i for i in list(string.punctuation)]
        ask = module.strreplace(ask, j); ask = module.strreplace(ask, not_goods)
        talks2 = []
        for i in talks:
            talks2 += talks[i]
        for i in [i.lower() for i in module.Replace(talks2, j)] + goodbyes + idks + hellos:
            (asked, good) = (i, True) if i in ask else (None, False)
            if good: break
            
        if not good: print("Sorry, I don't have that skill yet.")
        else:
            if ask == "what can we talk about" or ask in idks:
                k = set()
                while len(k) != 5:
                    k.add(random.choice(talks2))
                print(f"\nHere are some current options:\n\n******************************")
                for i in k:
                    print(f"\u2022 {string.capwords(name)}, {i}" + ("?" if "." not in i else ""))
                print("******************************\n")
            elif ask == '': print(random.choice(harry))
            elif ask in hellos:
                print(f"{str.capitalize(ask)}, {player}! What can I do for you?")
            elif ask in goodbyes:
                print(f"Goodbye, {player}! See you next time!")
                again = False
            else:
                file = [i for i in talks if asked in [i.lower() for i in module.Replace(talks[i], j)]][0]
                exec(open(directory + file + ".py").read())
                print("\nWhat do you want to talk about?")
