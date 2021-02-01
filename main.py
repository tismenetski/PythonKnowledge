# def main():
#     print("Jello")
#     arr = [2,5,2]
#     print(arr)
#
#
#
# if __name__ == "__main__":
#     main()


#input = input("What is your name? ")
#print(len(input)) # Length of string


s = "Hello"
print(s[0])


print(123 + 222)
number = 123_456_789 # underscore allows us to read the number more comfortably

#Float
number = 3.14159
print("Type of number is " + str(type(number))) # Print the type

#Boolean

answer = True
answer = False

newStr = str(number)

print(type(newStr))


result = 6 ** 2 # Power
print(result)


# height = input("Please enter your height: ")
# weight = input("Please enter your weight: ")
#
# bmi = float(weight) / (float(height) **2)
# #print(bmi)
# print("Your BMI is "+ str(bmi))
#
#
# print(round(bmi))

print(round(2.555555,2)) # 2.56
print(8 // 3) # result is 2 : chops the decimal , and type is INT
print(4/2) # result is 2.0 and the type is FLOAT


score = 0
height = 1.8
isWinning = True

#f-String --> allows to print multiple values together regardless of their types
print(f"your score is {score}, height is {height} and game status is {isWinning}")