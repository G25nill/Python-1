
import random

# Possible moves
moves = ["rock", "paper", "scissors"]

# Keep track of scores
player_score = 0
ai_score = 0

# Get player's move
def get_player_move():
    while True:
        player = input("Enter rock, paper or scissors: ").lower()

        if player in moves:
            return player
        else:
            print("Invalid move! Try again.")

# AI randomly selects a move
def get_ai_move():
    return random.choice(moves)

# Determine the winner
def determine_winner(player, ai):
    global player_score, ai_score

    print("You chose:", player)
    print("AI chose:", ai)

    if player == ai:
        print("It's a tie!")

    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        print("You win!")
        player_score += 1

    else:
        print("AI wins!")
        ai_score += 1

# Main game function
def play_game():
    global player_score, ai_score

    print("Welcome to Rock Paper Scissors!")

    while True:
        player = get_player_move()
        ai = get_ai_move()

        determine_winner(player, ai)

        print("\nYour score:", player_score)
        print("AI score:", ai_score)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again != "yes":
            print("\nFinal Score")
            print("Your score:", player_score)
            print("AI score:", ai_score)
            print("Thanks for playing!")
            break

# Start the game
play_game()
