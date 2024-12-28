import random

def game(enter):
    words = ["Rock", "Paper", "Scissor"]
    random_choice = random.choice(words)
    print(f"You Chose: {enter} and Computer chose: {random_choice}")
    if enter not in words:
        print("Invalid Input")
    elif enter == random_choice:
        print("Tie")
    elif (enter == "Rock") and (random_choice == "Scissor"):
        print("You Won")
    elif (enter == "Paper") and (random_choice == "Rock"):
        print("You Won")
    elif (enter == "Scissor") and (random_choice == "Paper"):
        print("You Won")
    else:
        print("You Lose")

print("Choose any one: Rock, Paper, Scissor")
a = input().title()
game(a)
