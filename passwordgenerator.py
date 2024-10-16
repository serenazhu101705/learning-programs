import random


while True:
    print("\nDo you want me to generate a password for you?")
    answer=input().lower()


    if answer=="no":
        print("\nGoodbye then.")
        break



    if answer=="yes":
        print("\nHow many lowercase letters do you want in your password?")
        lowers_answer=int(input())
        print("\nHow many capital letters do you want in your password?")
        capitals_answer=int(input())
        print("\nHow many numbers do you want in your password?")
        numbers_answer=int(input())
        print("\nAnd finally, how many special characters(ex.&,#) do you want in your password?")
        specials_answer=int(input())


        lowers=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        uppers=[str.capitalize(i) for i in lowers]
        digits = [str(i) for i in range(0,9)]
        specials = ["_","-",".","?","/",":",";","<",">","+","=","!","@","#","$","%","^","&","*","~","`"]

        a=random.sample(lowers,lowers_answer)
        b=random.sample(uppers,capitals_answer)
        c=random.sample(digits,numbers_answer)
        d=random.sample(specials,specials_answer)

        password=''.join(a+b+c+d)
        print(password)
        #convert 'password' to string
        #print(''.join(password))
        

    else:
        print("\nI'm sorry, you must type either Yes or No below.")


