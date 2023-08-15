import random


def guess_the_number():
    print("\nLet's play Guess The Number\n")

    x = int(input("Please chose a number range: "))
    if x <= 1:
        print("HEY! You can't chose 0 or 1 for a range.")
        return guess_the_number()
    random_number = random.randint(1, x)

    num_guesses = 0
    while True:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        num_guesses += 1

        if guess == random_number:
            print(f"Congrats! You've guessed the number {random_number} correctly in {num_guesses} guesses!")
            break
        elif guess < random_number:
            print('Too low!')
        else:
            print('Too high!')

