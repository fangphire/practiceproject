import random as rng

options = ["Rock", "Paper", "Scissors"]

gameStatus = "Y"

while gameStatus == "Y":

    ai_choice = options[rng.randint(0, 2)]

    playerChoice = input("Enter your choice: (Rock/Paper/Scissors) ")

    print("The AI chose", ai_choice)

    score = 0
    ai_score = 0

    if playerChoice == ai_choice:
        print("Game tied! ")


    elif playerChoice == "Rock" and ai_choice == "Paper":
        print("You lose! ")
        ai_score = ai_score+1

    elif playerChoice == "Scissors" and ai_choice == "Rock":
        print("You lose! ")
        ai_score = ai_score+1

    elif playerChoice == "Paper" and ai_choice == "Scissors":
        print("You lose! ")
        ai_score = ai_score+1

    elif playerChoice == "Rock" and ai_choice == "Scissors":
        print("You win! ")
        score = score+1

    elif playerChoice == "Paper" and ai_choice == "Rock":
        print("You win! ")
        score = score+1

    elif playerChoice == "Scissors" and ai_choice == "Paper":
        print("You win! ")
        score = score+1

    seeScore = input("Would you like to see your scores? (Y/N) ")

    if seeScore == "Y":
        print("Your score is", score, "and the AI's score is", ai_score)

    elif seeScore == "N":
        pass

    else:
        print("Wrong input, skipped scoreboard")

    gameStatus = input("Do you wish to continue playing? (Y/N) ")






    
























