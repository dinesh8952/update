import random

def guess_number():
    number = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Sorry, try again.")

if __name__ == "__main__":
    guess_number()
