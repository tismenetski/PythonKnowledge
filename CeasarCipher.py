alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(text_input, shift_input):
    encoded = ""
    for i in text_input:
        index = alphabet.index(i)
        if (index+shift_input) >= len(alphabet):
            #index =  + shift_input - index
            i = alphabet[len(alphabet)-1 + shift_input - index-1]
        else:
            i = alphabet[index+shift_input]  # Working with chars --> here we change(increment) char values
        encoded = encoded + i

    print(f"The encoded message is {encoded}")


def decrypt(text_input, unshift):
    decoded = ""

    for i in text_input:
        index = alphabet.index(i)
        if (index-unshift) < 0:
            index = len(alphabet) - unshift + index
        i = chr(ord(alphabet[index]) - unshift)  # Working with chars --> here we change(increment) char values
        decoded = decoded + i


encrypt(text, shift)



# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
