row1 = ["🥸", "🥸", "🥸"]
row2 = ["🥸", "🥸", "🥸"]
row3 = ["🥸", "🥸", "🥸"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to place the treasure? (first number is row , second is column")
inputRow = int(position[0])
inputColumn = int(position[1])


selectedRow = map[inputRow-1]
selectedRow[inputColumn-1] = "X"






print(f"{row1}\n{row2}\n{row3}")
