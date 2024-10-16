import random
print("I'm thinking of a number from 1 to 100\n")
print("Guess by typing in your number below\n")
x=random.randint(1,10)
for i in range(0,7):
    n = input("\nPlease pick a #:")
    if int(n)==x:
        print("That's Correct!")
        break
    else:
        if int(n)>x:
            print("That's too big")
        if int(n)<x:
            print("That's too small")
        if i==6:
            print("you are out of luck! the correct number is " + str(x))
