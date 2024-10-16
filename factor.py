#GCF of two numbers
print("Give me two numbers below and I will tell you the Least Common Multiple!")


#GCF
while True:
    print("\nType a number:")
    y=int(input())
    print("\nType another number:")
    z=int(input())
    a=[]
    for i in range(1,min(y,z)+1):
        if y%i==0 and z%i==0:
            a.append(i)

    #LCM
    one=y/max(a)
    two=z/max(a)
    lcm=one*two*max(a)
    print("The Least Common Multiple of " + str(y) + " and " + str(z) + " is " + str(lcm))

    print("\n\n\nDo you want to do this again? Type Yes or No below.")
    answer=input().lower()

    if answer=="no":
        print("Ok, thanks for doing this!")
        break
