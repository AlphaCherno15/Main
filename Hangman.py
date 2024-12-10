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

word_list = [
    # Nature & Environment
    "forest", "ocean", "river", "mountain", "desert", "rain", "thunder", "snow", 
    "volcano", "earthquake", "waterfall", "hurricane", "eclipse", "meadow", "glacier", 
    "coral", "canyon", "lagoon", "breeze", "sunset", "sunrise", "aurora", "prairie", 
    "oasis", "valley",

    # Animals
    "tiger", "eagle", "shark", "dolphin", "elephant", "panda", "penguin", "giraffe", 
    "koala", "whale", "cheetah", "bear", "wolf", "falcon", "rabbit", "octopus", "snake", 
    "spider", "frog", "lizard", "horse", "deer", "fox", "hawk", "owl",

    # Colors
    "red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", 
    "white", "grey", "cyan", "magenta", "turquoise", "beige", "lavender", "maroon", 
    "teal", "peach", "amber",

    # Food & Drink
    "pizza", "burger", "pasta", "steak", "sushi", "taco", "sandwich", "salad", "soup", 
    "cheese", "chocolate", "coffee", "tea", "juice", "milkshake", "icecream", "cake", 
    "bread", "honey", "bacon", "avocado", "apple", "banana", "strawberry", "orange",

    # Occupations
    "doctor", "engineer", "teacher", "artist", "pilot", "farmer", "chef", "musician", 
    "actor", "scientist", "writer", "architect", "detective", "athlete", "lawyer", 
    "mechanic", "nurse", "dentist", "photographer", "journalist", 

    # Technology
    "computer", "phone", "tablet", "keyboard", "mouse", "printer", "camera", "drone", 
    "robot", "satellite", "wifi", "software", "hardware", "battery", "circuit", 
    "screen", "sensor", "server", "chip", "gadget", 

    # Travel & Transportation
    "car", "plane", "boat", "train", "bus", "bicycle", "truck", "helicopter", 
    "submarine", "scooter", "motorcycle", "ship", "taxi", "jet", "glider", "camper", 
    "caravan", "cruise", "skateboard", "balloon", 

    # Emotions & Feelings
    "happy", "sad", "angry", "excited", "scared", "surprised", "lonely", "jealous", 
    "proud", "confident", "grateful", "nervous", "curious", "calm", "hopeful", "relaxed", 
    "tense", "shy", "brave", "loving",

    # Miscellaneous
    "clock", "book", "pen", "map", "star", "candle", "mirror", "key", "chair", 
    "table", "window", "door", "lamp", "bottle", "basket", "paper", "bag", "coin", 
    "flag", "ball", "dice", "card", "brush", "paint", "glove", "hat", "scarf", 
    "boot", "shoes", "cup", "plate", "knife", "fork", "spoon", "towel", "pillow", 
    "blanket", "curtain", "fan", "rope", "net", "chain", "lock", "helmet", "shirt", 
    "pants", "skirt", "watch", "ring", "necklace", "earrings", "belt", "wallet", 
    "umbrella", "binoculars", "compass", "bagpack", "lantern", "radio", "remote", 
    "brush", "comb", "soap", "shampoo", "mirror", "sunscreen", "clock", "thermometer",
]
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
