def migratoryBirds(arr):
    # Write your code here

    number = {}
    key = []

    for num in arr:
        if num not in number:
            number[num] = 1

        else:
            number[num] += 1

    for keys, values in number.items():
        if values == max(number.values()):
            key.append(keys)

    return min(key)
