import random

while True:
    computer_list = ["Rock","Paper","Scissors"]
    print("Type Rock, Paper, or Scissors below")
    player = input().capitalize()
    computer = random.choice(computer_list)

    if player not in computer_list:
        print("That's not funny")

    if player in computer_list:
        print("The computer chose " + computer)
        if player == computer:
            print("You tied!")

        else:
            if (player == "Rock" and computer == "Scissors") or (player == "Scissors" and computer == "Paper") or (player == "Paper" and computer == "Rock"):
                print("You won!")
            else:
                print("You lose.")



    print("Play again?")
    answer = input().lower()
    if answer == "no":
        print("Thanks for playing! Goodbye!")
        break


