def nb_dig(n, d):
    # your code
    count = 0
    for k in range(0, n+1):
        print(str(k*k))
        count += str(k*k).count(str(d))
    print(count)
    return count

nb_dig(10, 1)

