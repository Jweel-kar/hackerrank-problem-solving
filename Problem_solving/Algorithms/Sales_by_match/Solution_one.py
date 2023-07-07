def sockMerchant(n, ar):
    # Write your code here

    pairs = {}
    number = 0

    for i in ar:
        if i not in pairs:
            pairs[i] = 1
        else:
            pairs[i] += 1
    for key, value in pairs.items():
        if 2 <= value:
            num = value / 2
            num = int(num)
            number += num

    return number

