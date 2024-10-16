import random

while True:
    sum=0
    alist = ["You should become a pilot","You should become a video game designer","You should become a coder","You should become a CEO"]
    zlist = ["You should become a baseball player","You should become a basketball player","You should become a football player","You should become a soccer player","You should become a swimmer","You should become an author","You should become a engineer","You should become a cashier"]
    clist = ["You should become a teacher","You should become a lawyer","You should become a scientist","You should become an archaeologist","You should become a biomedical researcher","You should become a CFO"]
    dlist = ["You should become a doctor","You should become a chef"]
    print("You have entered a realm where we will decide what job fits you\n")
    print("answer the questions below\n\n\n")
    print("Do you like jobs that involve people,or do you like jobs that involve sitting around in your office?")
    print("1. Jobs with people\n")
    print("2. Sitting in a office\n")
    job=input()
    sum=sum+int(job)
    print("Do you like to sleep in,or do you like to wake up early?\n")
    print("1. Sleeping in\n")
    print("2. Waking up early\n")
    waking=input()
    sum=sum+int(waking)
    print("Do you like to work in a calm space,or a loud space?\n")
    print("1. Calm space\n")
    print("2. Loud space\n")
    space=input()
    sum=sum+int(space)
    print("Do you like technology,or do you like jobs with money?\n")
    print("1. Technology\n")
    print("2. Jobs with money\n")
    tech=input()
    sum=sum+int(tech)
    print("Do you like to do things with crafting,or do you like to do things with movement?\n")
    print("1. Crafting\n")
    print("2. Things with movement\n")
    topic=input()
    sum=sum+int(topic)
    print("What are you best at?\n")
    print("1. Sports\n")
    print("2. Education\n")
    print("3. Crafts\n")
    print("4. Weapons\n")
    best=input()
    sum=sum+int(best)
    print("Do you like to protect places and people,or do you like to save the enviroment?\n")
    print("1. Protect places and people\n")
    print("2. Save the enviroment\n")
    protect=input()
    sum=sum+int(protect)
    print("Do you like to things that everyone else does,or do you like to do things that you like?\n")
    print("1. Do everything that everyone does\n")
    print("2. You like to do things just by what you like\n")
    mind=input()
    sum=sum+int(mind)
    print("What are you best at\n?")
    print("1. Communicating\n")
    print("2. Independent work\n")
    print("3. Both")
    good=input()
    sum=sum+int(good)
    #quiz= [job,waking,space,tech,topic,best,protect,mind,good]
    if sum==14:
        print(alist[random.randint(0,len(alist)-1)])
    if sum==15:
        print(clist[random.randint(0,len(clist)-1)])
    if sum==20:
        print("You should become a policeman")
    if sum==16:
        print(zlist[random.randint(0,len(alist)-1)])
    if sum==13:
        print(dlist[random.randint(0,len(dlist)-1)])
    if sum==9:
        print("You should become a politician")

    print("\nDo you want to play again? Type Yes or No below.")
    answer=input().lower()

    if answer=="no":
        print("Ok, thanks for playing! Be sure to follow your dream!")
        break
