# Number divisible by 3 fizz
# Number divisible by 5 buzz
# Number divisible by 3 and 5 fizzbuzz

for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)

