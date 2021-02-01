import random

random_integer = random.randint(1, 10)

random_float = random.random()
random_float = random.random() * 5  # Random float between 0-5
print(random_integer)
print(random_float)
# a = random.randrange(0,5)
# print(a)

states = ["Alabama", "Delaware"]

states.append("New Mexico") # Add element to array


states.extend(["New York","Washington"]) # Add List to existing list


print(states)
