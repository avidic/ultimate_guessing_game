import random

def play_game():
    print("\n🎮 WELCOME TO THE ULTIMATE GUESSING GAME 🎮")
    print("Choose difficulty:")
    print("1 - Easy (1 to 10, 5 lives)")
    print("2 - Medium (1 to 50, 7 lives)")
    print("3 - Hard (1 to 100, 10 lives)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        max_number = 10
        lives = 5
    elif choice == "2":
        max_number = 50
        lives = 7
    elif choice == "3":
        max_number = 100
        lives = 10
    else:
        print("Invalid choice. Defaulting to Easy.")
        max_number = 10
        lives = 5

    number = random.randint(1, max_number)
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {max_number}.")

    while lives > 0:
        guess = input("Take a guess: ")

        if not guess.isdigit():
            print("⚠️ Please enter a real number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess == number:
            print(f"🎉 YOU WIN in {attempts} attempts!")
            return attempts
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

        lives -= 1
        print(f"Lives left: {lives}")

    print(f"💀 You lost! The number was {number}")
    return 0


score = 0

while True:
    result = play_game()
    score += result
    print(f"\n🏆 Your total score: {score}")

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! 😎")
    try:
    with open("highscore.txt", "r") as f:
        highscore = int(f.read())
except:
    highscore = 0

if score > highscore:
    with open("highscore.txt", "w") as f:
        f.write(str(score))
    print(f"🏆 NEW HIGH SCORE: {score}!")
else:
    print(f"Current high score: {highscore}")
        break