import random
while True:
    computer_choices = ['r', 'p', 's']
    your_choice = input("rock/paper/scissors?(r/p/s)").lower()
    if your_choice not in computer_choices:
        print("invalid choice")
        continue
    comp = random.choice(computer_choices)
    print(f"you choosed: {your_choice}")
    print(f"computer choosed:  {comp}")
    if comp == your_choice:
        print("tie!")
    elif (comp == 'r' and your_choice == 's') or\
        (comp == 'p' and your_choice == 'r') or\
            (comp == 's' and your_choice == 'p'):
        print(f'you lose')
    else:
        print('you win')
    again = input("yes to continue y\n? : ").lower()

    if again == 'n':
        break
