import random


def pass_gen(chars, length):
    new_pass = ''
    for i in range(1, length - 1):
        if i == 1:
            new_pass += str(random.choice(chars[0:26]))
        if i == 3:
            new_pass += str(random.choice(chars[-2:]))
        new_pass += str(random.choice(chars[27:-2]))
    return new_pass


chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '#', '$']
length = 8
print(pass_gen(chars, length))
