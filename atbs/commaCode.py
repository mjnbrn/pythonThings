def commacode(thelist):
    if thelist == []:
        return "Please give me a list!"
    theString = ''
    for i in range(len(thelist)):
        if i < len(thelist) - 1:
            theString += thelist[i] + ', '
        else:
            theString += 'and ' + thelist[i]
    return theString


spam = ["Alpha", "Bet"]
print(commacode(spam))
