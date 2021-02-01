import random

userChoice = int(input("What do you choose? Type 0 for Rock , 1 For Paper and 2 For Scissors\n"))
cpuChoice = random.randint(0, 2)


print(f"Computer chose {cpuChoice}")

if userChoice == 0 and cpuChoice == 2:
    print("You win!")
elif userChoice == 1 and cpuChoice == 0:
    print("You win!")
elif userChoice == 2 and cpuChoice == 1:
    print("You win!")
elif userChoice == cpuChoice:
    print("Draw!")
elif not (0 <= userChoice <= 2):
    print("Wrong input by user")
else:
    print("You Lose!")
