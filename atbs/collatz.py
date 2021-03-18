def collatz(number):
    if number % 2 == 0:
        r = number // 2
        print(r)
        return r
    else:
        r = 3 * number + 1
        print(r)
        return r


print('Please type an integer')
while True:

    try:
        number = int(input())
        break
    except ValueError:
        print("Please enter a valid integer")


while number > 1:
    number = collatz(number)