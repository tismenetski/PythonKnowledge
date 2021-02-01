import random

namesString = input("Give me the list of names, seperated by comma: ")
names = namesString.split(",")

print(names)

randomNumber = random.randint(0,len(names)-1)

print(randomNumber, names[randomNumber])

fruits = ["Strawberries","Peaches","Nectarines","Apples","Cherries","Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirtyDozen = [fruits, vegetables]

print(dirtyDozen)