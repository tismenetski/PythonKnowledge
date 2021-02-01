print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    print("You can ride the roller coaster")
    age = int(input("What is your age? "))
    if age >= 18:
        print("Adult tickets are 12")
        bill = 12
    elif 12 < age < 18:
        print("Adult tickets are 7")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything will be ok, have a free ride on us!")
    else:
        print("Adult tickets are 5")
        bill = 5
    wantsPhoto = input("Do you want a photo taken? Y or N ")
    if wantsPhoto == 'Y':
        # Add $3 to their bill
        bill += 3

    print(f"Final ticket price is {bill}")
else:
    print("Sorry, you have to grow taller before you ride")
