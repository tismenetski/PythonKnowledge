#Calculator


def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    '+' : add,
    '-' : substract,
    '*' : multiply,
    '/' : divide
}


def calculator():

        should_continue = True
        num1 = int(input("What's the first number?: "))
        while should_continue:


            print("Which operation you want to do?")
            for operation in operations:
                print(operation)
            operation = input("Selection: ")

            num2 = int(input("What's the next number?: "))

            calculation_function = operations[operation]
            answer = calculation_function(num1,num2)

            print(f"{num1} {operation} {num2} = {answer}")
            selection = input("Continue with operations on current number or exit (c - continue e - exit)")
            if selection != 'c':
                should_continue = False
                calculator()
            else:
                num1 = answer





calculator()