
##while True:
##    print("\n\nType a number below and I will tell whether it's a prime number or not")
##    x=int(input())
##    found=True
##
##
##    for i in range(2,x):    
##        if x%i == 0:
##            found = False
##            break
##    if found:
##        print("\nIt's a prime number")
##
##    else:
##        print("\nIt's not a prime number")
##    print("\nDo you want want to do this again? Type Yes or No below.")
##    answer=input().lower()
##
##    if answer=="no":
##        print("\nOk, thanks for doing this!")
##        break
##
##
##
while True:

    print("\n\nType a number below and I will find all the prime numbers between 1 and that number!\n")
    x=int(input())
    a=[2]

    for i in range(3,x+1,2):
        isPrime=True

        for y in range(2,i):        
            if i%y == 0:
                isPrime = False
                break

        if isPrime:
            a.append(i)
            
    print("Here it is:\n"+str(a))
    print("\nDo you want to do this again? Type Yes or No below.")
    answer=input().lower()

    if answer=="no":
        break

##
##
##def isPrime():
##    print("\n\nType a number below and I will find all the prime numbers between 1 and that number!\n")
##    x=int(input())
##    a=[2]
##
##    for i in range(3,x+1,2):
##        isPrime=True
##
##        for y in range(2,i):        
##            if i%y == 0:
##                isPrime = False
##                break
##
##        if isPrime:
##            a.append(i)


def ha(number):
    x=number
    found=True


    for i in range(2,x):    
        if x%i == 0:
            found = False
            break
    if found:
        print("\nIt's a prime number")

    else:
        print("\nIt's not a prime number")
