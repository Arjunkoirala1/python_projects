# generate random number from 1 to 100
# make user to guess
# if the number is too high then  print very high
# else if the number is too low then print very low
# else if the random number match the guess then print congratulation

import random
g1 = random.randint(1, 100)

print(g1)
while True:

    y1 = int(input('guess the number from 1 to 100:  '))
    if y1 > g1:
        print("high bru")
    elif y1 < g1:
        print("low bru")
    else:
        print("congratulations bru")
