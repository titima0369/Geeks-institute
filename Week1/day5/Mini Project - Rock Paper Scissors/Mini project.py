import random

print("Welcome to Rock, Paper, Scissors!")
print("Type rock, paper, or scissors to play. Type quit to stop.\n")


wins = 0
losses = 0
draws = 0

while True:
    user_choice = input("Your choice (rock/paper/scissors): ").lower()

    if user_choice == "quit":
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.\n")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!\n")
        draws += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!\n")
        wins += 1
    else:
        print("You lose!\n")
        losses += 1

print("\nGame Over! Here are your results:")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"Draws: {draws}")
print("Thanks for playing!")