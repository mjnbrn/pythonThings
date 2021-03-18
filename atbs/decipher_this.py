def decipher_this(string):
    import re
    deciphered = []
    for word in string.split(' '):
        if word.isnumeric():
            deciphered.append(chr(int(word)))
        else:
            reg = re.search('([0-9]+)(.*)', word)
            cipherstring = reg.groups()[1]
            if len(cipherstring) == 1:
                deciphered.append(f'{chr(int(reg.groups()[0]))}{cipherstring[0]}')
            elif len(cipherstring) == 2:
                deciphered.append(f'{chr(int(reg.groups()[0]))}{cipherstring[-1]}{cipherstring[0]}')
            else:
                deciphered.append(f'{chr(int(reg.groups()[0]))}{cipherstring[-1]}{cipherstring[1:-1]}{cipherstring[0]}')
    return ' '.join(deciphered)


print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))