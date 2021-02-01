studentHeights = input("Input a list of student heights: ").split()  # Student heights splitted by a comma
sum = 0
average = 0
for height in studentHeights:
    sum += int(height)

average = sum / len(studentHeights)

print(average)
# Range
total = 0
for number in range(2, 101, 2):
    total += number
    print(number)

print(total)

total2 = 0
for number in range(2,101):
    if number % 2 == 0:
        total2 += number

print(total2)
