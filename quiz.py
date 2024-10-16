import random
sum=0
clist = ["You are a Graveyard! You have many friends and you came back from the dead!", "You are a Lava Hound! You first live a long happy life, but when you die, you live six angry short lives! YAY!"]
dlist = ["You are a Bandit! You love to die your hair white and black because your favorite animal is a panda!", "You are an Inferno Dragon! You have a master and you get whipped everytime you won't obey! Have fun!", "You are a Fisherman! You are too poor to afford a weapon so you stole a magical fish! So not embarassing, like, duh!", "You are a Sparky! You are programmed to destroy anything on site, meaning you will be forever lonely.", "You are a Mega Knight! You are overweight and everyone is afraid of your obesity! OMG!", "You are a Log! Well, you are a log. There's really nothing more I can say.","You are a Lumberjack! The stuff you drink is as bad as marajuana. OMG!"]
elist = ["You are an Ice Wizard! But you still have to wear a fur coat. No one knows why.", "You are an Electro Wizard! You got your powers by being smushed under a rock while being electrocuted every five seconds. Also, you have a movie about your pirate days. YAY!"]
flist = ["You are a Miner! Your life is based off on a candle on your head! OMG!", "You are a Princess! You have a secret admirer called Prince and you hate him."]
print("What Legendary Clash Royale Character are you?\n")
print("Take this quiz to find out!\n\n\n\n\n\n")
print("Do you like Offense or Defense cards?\n")
print("1. Offense\n")
print("2. Defense\n")
offense=input()
sum = sum + int(offense)
print("Do you like to paralyze people or do you like to clone yourself?\n")
print("1. Paralyze\n")
print("2. Clone\n")
clone=input()
sum = sum + int(clone)
print("Would you rather slow people down or push people back?\n")
print("1. Slow people down\n")
print("2. Push people back\n")
slow=input()
sum = sum + int(slow)
print("Would you rather go anywhere you want or move really fast?\n")
print("1. Go anywhere I want\n")
print("2. Move really fast\n")
fast=input()
sum = sum + int(fast)
print("Would you rather want many friends or be really good at math?\n")
print("1. Have many friends\n")
print("2. Be really good at math\n")
math=input()
sum = sum + int(math)
print("Would you rather want to hook people or fly?\n")
print("1. Hook people\n")
print("2. Fly, like, duh\n")
fly=input()
sum = sum + int(fly)
print("Would you rather breath out fire or shock people with electricity?\n")
print("1. Breath out fire\n")
print("2. Shock people\n")
fire=input()
sum = sum + int(fire)
print("Would you rather be small and annoying or blast anything out of your sight?\n")
print("1. Be small and annoying\n")
print("2. Blast anything out of my sight\n")
blast=input()
sum = sum + int(blast)
print("Would you rather be invisible or dash on to people?\n")
print("1. Invisible\n")
print("2. Dash onto people\n")
dash=input()
sum = sum + int(dash)
print("Would you rather be slow and strong, fast and weak, or mediocre at both?\n")
print("1. Slow but strong\n")
print("2. Fast but weak\n")
print("3. Mediocre\n")
slow=input()
sum = sum + int(slow)
#quiz= [offense, clone, slow, fast, math, fly, fire, blast, dash, slow]
if sum==14:
        print("You are Royal Ghost! Ooooooooooh!")
if sum==16:
        print("You are a Ram Rider! You love to eat grass!")
if sum==12:
        print(clist[random.randint(0,len(clist)-1)])
if sum==19:
        print("You are a Magic Archer! Your favorite subject is Geometry!")
if sum==15:
        print(dlist[random.randint(0,len(dlist)-1)])
if sum==17:
        print(elist[random.randint(0,len(elist)-1)])
if sum==18:
        print("You are a Night Witch! Your only friends are bats!")
if sum==13:
        print(flist[random.randint(0,len(flist)-1)])

else:
    print("\nCongratulations! You have hacked the System!")
    print("Welcome, Joe Mama!")

    
