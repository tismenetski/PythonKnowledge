print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S,M,L")
addPepperoni = input("Do you want pepperoni? Y/N")
extraCheese = input("Do you want extra cheese? Y/N")

# Small pizza 15 , medium 20 , large 25
# pepperoni for small: 2 , pepperoni for medium or large: 3
# extra cheese for any pizza : 1


amount = 0
if size == 'S':
    amount += 15
    if addPepperoni == 'Y':
        amount += 2
elif size == 'M':
    amount += 20
    if addPepperoni == 'Y':
        amount += 3
elif size == 'L':
    amount += 25
    if addPepperoni == 'Y':
        amount += 3
if extraCheese == 'Y':
    amount+=1

print(f"Final Price is {amount}")