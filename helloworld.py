import random
print("I'm thinking of a number from 1 to 100\n")
print("Guess by typing in your number below\n")
x=random.randint(1,100)
for i in range(0,5):
    n = input("Please pick a #:")
    if int(n)==x:
        print("That's Correct!")
        break
    else:
        if int(n)>x:
            print("That's too big")
        if int(n)<x:
            print("That's too small")
        if i==4:
            print("you are out of luck! the correct number is " + str(x))
