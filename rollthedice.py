import random


while True:
    w=random.randint(1,6)
    x=random.randint(1,6)
    y=random.randint(1,6)
    z=random.randint(1,6)
    alist=[w,x]
    blist=[y,z]
    bigger_number=max(sum(alist),sum(blist))
    
    ##present options
    print("\n\nI'm going to roll 4 dice, guess which pair's sum is larger\n")
    print("1. The first and second dice")
    print("2. The third and fourth dice\n")
    selected=int(input())


    if selected == 1:
        pair = sum(alist)
    else:
        pair = sum(blist)



    ##responses
    if pair == bigger_number:
        print("\nYou got it right! Good job!")
    else:
        print("\nSorry wrong guess")

    print("\nthe first two dice were a " + str(w) + " and " + str(x))
    print("the last two dice were a " + str(y) + " and " + str(z))



    ##play again?
    print("\n\n\nDo you want to play again?(Yes/No)\n")
    play=input().lower()


    ##end
    if play=="no":
        print("\nOk, thanks for playing!")
        break






        
##    if x == j:
##        print("You got it right! Good job!")
##    else:
##        print("Sorry wrong")
##    print("The first die was a " + str(x) + " and the second one was a " + str(y))
##else:
##    if y==j:
##        print("You got it right! Good job!")
##    else:
##        print("Sorry, the first die was a " + str(x) + " and the second one was a " + str(y))
##
    

    
