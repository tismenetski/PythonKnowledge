

age = int(input("What is your age in years? "))
currentWeeks = age*365 / 52

# print(f"{currentWeeks}")
max = 90

yearsLeft = max - age

print(f"You have {yearsLeft*365} days, {yearsLeft*52} weeks and {yearsLeft*12} months left")
