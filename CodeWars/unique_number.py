def find_uniq(arr):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]   # n: unique integer in the array
    else:
        return arr[-0]


find_uniq([ 1, 1, 1, 2, 1, 1 ])