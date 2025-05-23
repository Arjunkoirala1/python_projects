# dice rolling game

# loop
# ask user roll dice
# if enters yes
# generate random numbers
# if n then say tahnkyou and terminate
# else invalid choice
import random
while True:

    command = input("do you ant to roll the dice y/n?").lower()
    if command == 'y':
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print(f'({d1},{d2})')
    elif command == 'n':
        print("good bye")
    else:
        print("invalid choice")
