import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========
''', '''
  +---+
  |   |
  O   |
 /|\  |
  |   |
      |
========
''', '''
  +---+
  |   |
  O   |
 /|\  |
  |   |
 /    |
========
''', '''
  +---+
  |   |
  O   |
 /|\  |
  |   |
 / \  |
========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for position in chosen_word:
    placeholder += "_"

game_over = False
correct_letters = []
incorrect_letters = []
lives = 7
stage = 0
print(stages[stage])
print(placeholder)

print(f'You have: {lives} Lives')
while not game_over:

    guess = input("Guess a letter: ").lower()
    display = ""

    if guess not in chosen_word:
        if guess in incorrect_letters:
            print(f'You tried {guess} and It is wrong')
        elif lives > 0:
            incorrect_letters.append(guess)
            lives -= 1
            stage += 1
            print(stages[stage])
            print(f'The word does not contain {guess}')
            print(f'You lost a live, {lives} lives left')
        else:
            print(stages[stage])
            print(f'You have {lives} Lives')

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        print("You won")
        print(f'The word was "{chosen_word}"')
        break
    elif lives == 0:
        print(f'You died')
        print(f'The word was "{chosen_word}"')
        break
