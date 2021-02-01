# If the bill was 150.00, split between 5 people , with 12% tip
# Each person should pay 150/5 * 1.12 = 33.6
# Round the result to 2 decimal places = 33.60


bill = float(input("Please write the bill sum: "))
tip = float(input("Please write the tip size you would like to give(10%,12%,15%): "))
dinners = int(input("Please write the number of people to split the bill: "))
tipAsPercent = tip /100
totalTipAmount = bill * tipAsPercent
totalBill = bill + totalTipAmount
billPerPerson = totalBill / dinners
finalAmount =round(billPerPerson,2)
finalAmount = "{:.2f}".format(billPerPerson)
#print(f"Each person should pay: {round((bill / dinners) * ((tip / 100) + 1), 2)}")
print(f"Each person should pay: ${finalAmount}")
