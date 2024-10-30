import random

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors or quit to stop): ").lower()
        
        if player_choice == "quit":
            print("Thanks for playing!")
            break
        elif player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)

# Start the game
play_game()
