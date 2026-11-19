import random

secret = random.randint(1, 100)
valid_attempts = 0
max_attempts = 7

while valid_attempts < max_attempts:
    guess = int(input("Guess the secret number (1-100): "))

    if guess < 1 or guess > 100:
        print("Out of range! Guess between 1 and 100.")
        continue

    valid_attempts += 1

    if guess == secret:
        if valid_attempts == 1:
            print("Perfect score! You guessed it on the first attempt!")
        else:
            print(f"Congratulations! You guessed it in {valid_attempts} attempts.")
        break
    elif guess < secret:
        print("Higher!")
    else:
        print("Lower!")
else:
    print(f"Game over! The secret number was {secret}.")