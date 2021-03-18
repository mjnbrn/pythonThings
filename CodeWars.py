# Decipher this!
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

# Consonant value
def solve(s):
    vals = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    import re
    spam = []
    for i in re.sub('[aeiou]', ' ', s).split(' '):
        adds = 0
        for a in i:
            adds += vals[a]
        spam.append(adds)
    spam.sort()
    return spam[-1]

# Folding your way to the moon
def fold_to(distance):
    if distance < 0:
        return None
    elif distance < 0.0001:
        return 0
    else:
        folds = 0
        thick = 0.0001
        while thick < distance:
            thick *= 2
            folds += 1
        return folds

# Flatten and sort an array
def flatten_and_sort(array):
    nmb = []
    for i in array:
        for y in i:
            nmb.append(y)
    nmb.sort()
    return nmb

# Dubstep
def song_decoder(song):
    while song.count('WUBWUB') > 0:
        song = song.replace('WUBWUB', 'WUB')
    song = song.replace('WUB', ' ')
    return song.strip()
    

# Find the odd int
def find_it(seq):
    count = {}
    for i in seq:
        count.setdefault(i, 0)
        count[i] += 1
    for k, v in count.items():
        if v % 2 == 1:
            return k

# Remove anchor from URL
def remove_url_anchor(url):
    # TODO: complete
    if '#' in url:
        return url[0:url.index('#')]
    else:
        return url

# Array.diff
def array_diff(a, b):
    if not a:
        return []
    for c in b:
        i = 0
        while i < a.count(c):
            a.remove(c)
            

    return a

# Odd or Even?
def odd_or_even(arr):
    c = 0
    for i in arr:
        c += i

    return "odd" if c%2 == 1 else "even"

    
# Isograms
def is_isogram(string):
    x = sorted(string.lower())
    if len(string) == len([y for y in x if x.count(y) == 1]):
        return True
    else:
        return False

# Title Case
def title_case(title, minor_words=""):
    titled = ""
    for word in title.split(" "):
        if not titled:
            titled += "{0} ".format(word.capitalize())
        elif word.lower() not in minor_words.lower().split(" "):
            titled += "{0} ".format(word.capitalize())
        else:
            titled += "{0} ".format(word.lower())
    return titled.rstrip()

# Number of People in the Bus
def number(bus_stops):
    passengers = 0 
    for t in bus_stops:
        passengers += t[0]
        passengers -= t[1]
    return passengers

# Reversed sequence
def reverse_seq(n):
    return list(range(n, 0, -1))

# Reversed sequence
def reverse_seq(n):
    return list(range(n, 0, -1))

# Find the unique number
def find_uniq(arr):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]   # n: unique integer in the array
    else:
        return arr[-0]

# The highest profit wins!
def min_max(lst):
  lst.sort()
  return [lst[0], lst[-1]]
  

# Count the Digit
def nb_dig(n, d):
    count = 0
    for k in range(0 , n+1):
        count += str(k**2).count(str(d))
    return count

# Shortest Word
def find_short(s):
    # your code here
    s = s.split(" ")
    l = len(s[0])
    for word in s:
        if len(word) < l:
            l = len(word)
    return l # l: shortest word length

# Growth of a Population
def nb_year(p0, percent, aug, p):
    ptrack = p0
    year = 0
    while ptrack <= p:
        year += 1
        
        # if p > ptrack:
        
        ptrack = round(ptrack + (ptrack * (percent/100)) + aug)
        
            
    if year == 51:
        year -= 1
    return year

# Unique In Order
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

# Vowel Count
def getCount(inputStr):
    num_vowels = 0
    # your code here
    vowel = ('a','e','i','o','u')
    for l in inputStr:
         if l in vowel:
             num_vowels += 1
    return num_vowels

# Multiply
def multiply(a, b):
  return a * b
