
def number_checker(number):

    div = 0
    for num in range(1, number):
        if number % num == 0:
            div += 1
    if div > 2:
        return False
    return True


n = int(input("Check this number: "))
print(number_checker(n))
