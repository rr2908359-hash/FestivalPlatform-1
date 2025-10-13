# Rock Paper Scissors Game
import random

def get_choice_name(choice):
    """Convert choice number to name."""
    choices = {0: "Rock", 1: "Paper", 2: "Scissors"}
    return choices.get(choice, "Invalid")

def determine_winner(player, computer):
    """Determine the winner of a round."""
    if player == computer:
        return "tie"
    elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        return "win"
    else:
        return "lose"

def get_valid_choice():
    """Get a valid choice from the user."""
    while True:
        try:
            choice = int(input("Enter your choice (0: Rock, 1: Paper, 2: Scissors): "))
            if choice in [0, 1, 2]:
                return choice
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_round():
    """Play a single round and return the result."""
    computer_choice = random.randint(0, 2)
    player_choice = get_valid_choice()
    
    print(f"You chose: {get_choice_name(player_choice)}")
    print(f"Computer chose: {get_choice_name(computer_choice)}")
    
    result = determine_winner(player_choice, computer_choice)
    if result == "win":
        print("You win this round!")
    elif result == "lose":
        print("You lose this round!")
    else:
        print("It's a tie!")
    
    return result

def play_series(num_rounds=3):
    """Play a series of rounds."""
    wins = 0
    losses = 0
    ties = 0
    
    print(f"\nStarting a best-of-{num_rounds} series!")
    print("You need to win at least half the rounds to win the series.\n")
    
    for round_num in range(1, num_rounds + 1):
        print(f"Round {round_num}:")
        result = play_round()
        if result == "win":
            wins += 1
        elif result == "lose":
            losses += 1
        else:
            ties += 1
        print()
    
    print("Series Results:")
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
    
    if wins > losses:
        print("You win the series!")
    elif losses > wins:
        print("You lose the series!")
    else:
        print("The series is a tie!")
    
    return wins, losses, ties

def main():
    """Main game loop."""
    print("Welcome to Rock Paper Scissors!")
    print("You will play against the computer.")
    
    while True:
        play_series()
        
        play_again = input("\nDo you want to play another series? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

