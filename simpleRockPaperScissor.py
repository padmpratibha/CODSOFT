import random


def play_game():

    choices = ["rock","paper","scissor"]
    while True:

        user_choice = input("enter your choice (Rock,Paper,Scissor) or enter Q to quit : ").lower()

        if user_choice not in choices:
            break           

        compuer_choice = random.choice(choices)
        print(f"computer choice : {compuer_choice}")

        if user_choice == compuer_choice:
            print("Its Tie!")
        elif (user_choice == 'rock' and compuer_choice == 'scissor') or\
                (user_choice == 'paper' and compuer_choice == 'rock') or\
                    (user_choice == 'scissor' and compuer_choice == 'paper'):
            print(" You Win !")
        else:
            print("You loose !")




if __name__ == "__main__":
    play_game()


