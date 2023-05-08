def reverseArray(a):
    # Write your code here

    rev = []
    length = len(a)

    for i in range(length-1, -1, -1):
        rev.append(a[i])
    return rev

