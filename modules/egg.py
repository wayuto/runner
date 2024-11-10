from random import randint

number: int = randint(0, 100)

def guess_number(guess: int) -> int:
    if guess > number:
        print("Too big")
        guess_number(int(input("Guess a number between 1~100: ")))
    elif guess < number:
        print("Too small")
        guess_number(int(input("Guess a number between 1~100: ")))

guess_number(int(input("Guess a number between 1~100: ")))
print(f"You won!")