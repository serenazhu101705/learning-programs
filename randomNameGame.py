import random
print("I'm thinking of a person in our family\n")
print("Try to guess by typing in the name of the person below\n\n")
blist = ["josh", "janet", "joyce", "serena", "justin"]
x=blist[random.randint(0,len(blist)-1)]
for i in range(0,3):
    n=input().lower()
    if n==x:
        print("That's Correct! Good guessing!")
        break
    else:
        if n!=x:
            print("Wrong. Try again.\n")
        if i==2:
            print("Sorry, the correct answer was " + str(x))


    
