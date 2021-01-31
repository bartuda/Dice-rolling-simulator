#source https://www.youtube.com/watch?v=pOzv5p745Hc&ab_channel=EasyCoding

import random

run = True

while run:
    user_input = input("Press enter to roll or type x to stop: ")

    if user_input == "x":
        run = False

    else:
        roll = random.randint(1,6)

        print(roll)
        print()

print()
print()
print("Thanks for playing")

