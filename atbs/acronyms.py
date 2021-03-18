def acro(nym):
    rv = ""
    for i in nym.split(' '):
        rv += i[0]
    return rv.upper()


print('Please input some words separated by space!')
stri = input()

print(acro(stri))