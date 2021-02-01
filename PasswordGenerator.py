
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# lettersAppended = 0
# numbersAppended = 0
# symbolsAppended = 0
# password = ""
# length = nr_letters + nr_numbers + nr_symbols
# for number in range(0, length):
#     rand = random.randint(0, 2)
#     if rand == 0 and lettersAppended < nr_letters:
#         randChar = letters[random.randint(0, len(letters)-1)]
#         print(randChar)
#         password = password.__add__(randChar)
#         lettersAppended += 1
#     elif rand == 1 and numbersAppended < nr_numbers:
#         randChar = numbers[random.randint(0, len(numbers)-1)]
#         print(randChar)
#         password = password.__add__(randChar)
#         numbersAppended += 1
#     elif rand == 2 and symbolsAppended < nr_symbols:
#         randChar = symbols[random.randint(0, len(symbols)-1)]
#         print(randChar)
#         password = password.__add__(randChar)
#         symbolsAppended += 1
#     else:
#         length += 1
#
#
# print(password)


# password = ""
# 
# for char in range(1, nr_letters+1):
#     password += random.choice(letters)
#     print(password)
# 
# for char in range(1, nr_numbers+1):
#     password += random.choice(numbers)
#     print(password)
# 
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#     print(password)
# 
# print(password)

passwordList = []

for char in range(1, nr_letters+1):
    passwordList += random.choice(letters)
    print(passwordList)

for char in range(1, nr_numbers+1):
    passwordList += random.choice(numbers)
    print(passwordList)

for char in range(1, nr_symbols + 1):
    passwordList += random.choice(symbols)
    print(passwordList)
    

random.shuffle(passwordList)
print(passwordList)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P