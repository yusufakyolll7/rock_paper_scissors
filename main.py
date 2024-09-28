import random

while True:
    user_action=input("Enter a choice(rock,paper,scissors): ").lower()
    possible_actions=["rock","paper","scissors"]

    if user_action not in possible_actions:
        print("You entered an invalid choice. Please enter rock, paper, or scissors.")
    else:
        comp_action = random.choice(possible_actions)
        print(f"\n You chose {user_action}, computer choose {comp_action}.\n")
        if user_action == comp_action:
            print(f"Both players selected {user_action}.So it is a tie!")
        elif user_action == "rock":
            if comp_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose!")
        elif user_action == "paper":
            if comp_action == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose!")
        elif user_action == "scissors":
            if comp_action == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose!")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() == "n":
            print("Goodbye")
            break



