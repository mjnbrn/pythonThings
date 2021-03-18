iterabble = 'AAAABBBCCDAABBB'


def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    count = 0
    prev = iterable[0]
    hold = []
    for i in iterable:
        if i == prev:
            if count == 0:
                hold.append(i)
            pass
        else:
            hold.append(i)
        prev = i
        count += 1
    return hold

unique_in_order('AAAABBBCCDAABBB')

def unique_in_order(iterable):
    count = 0
    prev = iterable[0]
    hold = []
    for i in iterable:
        if i == prev:
            if count == 0:
                hold += i
            pass
        else:
            hold += i
        prev = i
        count += 1
    return hold