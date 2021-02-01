programming_dictionary = {
    "Bug": "An error in a program",
    "Function": "A piece of code that you can easily call over and over again",

}


print(programming_dictionary)

programming_dictionary["Loop"] =  "The action of doing something again and again"  # Assign new key value pair to a
# dictionary

print(programming_dictionary)

empty_dictionary = {}


# Wipe existing dictionary

# programming_dictionary = {}
# print(programming_dictionary) # {}


# Loop through a dictionary

for key in programming_dictionary:
    print(key)  # Print only the key
    print(programming_dictionary[key])  # Print the value
