import random
a = 0
b = 100
number = random.randint(a, b)
base = 0
def check():
    x = 0
    b = []
    while True:
        max_range = 100
        guess = random.randint(0, max_range)
        if guess == max_range:
            break
        else:
            x += 1
            b.append(x)
    print(max(b))

# print(number)
print("Welcome to the Number Guessing Game!")
print(f'I am thinking of a number between {a} and {b}')
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
def diff(x):
    global base
    base = 0
    if x == "easy":
        base = 10
        return 10
    else:
        base = 5
        return 5
chances = diff(difficulty)

print(f'You have {chances} chances.')
def check_position(y):
    global chances
    if int(y) > number:
        print("you over")
        chances -= 1

    else:
        print("you under")
        chances -= 1

while True:
    print(f'You still have {chances} chances')
    player_guess = int(input("Make a Guess:"))
    if player_guess == number:
        print(f'You guessed, the number was {number}')
        break
    elif chances == 1:
        print(f'You out of chances, the number was {number}')
        break
    elif chances == 3 and base == 10 or chances == 2 and base == 5:
        hint = input("Do you want a hint? 'y' or 'n'")
        if hint == "y":
            if player_guess < number:
                distance = len(range(player_guess, number))
            else:
                distance = len(range(number, player_guess))
            print(f'You are {distance} away from the number')
    else:
        check_position(player_guess)
