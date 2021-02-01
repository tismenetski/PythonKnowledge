print("Welcome to love calculator")
name1 = input("Please Enter first name ")
name2 = input("Please enter second name ")

combinedName = name1 + name2
combinedName = combinedName.lower()


t = combinedName.count("t")
r = combinedName.count("r")
u = combinedName.count("u")
e = combinedName.count("e")
l= combinedName.count("l")
o= combinedName.count("o")
v = combinedName.count("v")


true = t + r + u + e
love = l + o + v + e

result = str(true) + str(love)
result = int(result)

if (result < 10) or (result > 90):
    print(f"Your love score is {result}, you go together like coke and mentos.")
elif (result >= 40) and (result <= 50):
    print(f"Your love score is {result}, you are alright together.")
else:
    print(f"Your score is {result}")

print(result)



#print(combinedName)
