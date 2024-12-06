import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]

def game():
    pc_choice = random.randint(0, 2)
    print("0 for rock, 1 for paper, 2 for scissors")
    player_choice = int(input("What is your choice?"))

    if pc_choice == player_choice:
        print("draw")
        print("your choice was and the PC choice was" + options[pc_choice])
    elif pc_choice == 0 and player_choice == 1:
        print("you won")
        print("your choice was:" + options[player_choice])
        print("The PC choice was:" + options[pc_choice])
    elif pc_choice == 0 and player_choice == 2:
        print("you lost")
        print("your choice was:" + options[player_choice])
        print("The PC choice was:" + options[pc_choice])
    elif pc_choice == 1 and player_choice == 0:
        print("you lost")
        print("your choice was:" + options[player_choice])
        print("The PC choice was:" + options[pc_choice])
    elif pc_choice == 1 and player_choice == 2:
        print("you won")
        print("your choice was:" + options[player_choice])
        print("The PC choice was:" + options[pc_choice])
    elif pc_choice == 2 and player_choice == 0:
        print("you won")
        print("The PC choice was:" + options[player_choice])
        print("The PC choice was:" + options[pc_choice])
    elif pc_choice == 2 and player_choice == 1:
        print("you lost")
        print("your choice was:" + options[player_choice])
        print("The PC choice was:" + options[pc_choice])
    else:
        print("you moron, Only whole number between 0 and 2")
i = 10 #just to play the game 10 times
for i in range(1, 11):
    game()
