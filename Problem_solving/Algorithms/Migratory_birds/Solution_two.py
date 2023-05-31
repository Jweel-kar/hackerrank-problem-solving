def migratoryBirds(arr):
    # Write your code here

    max_ids = []

    set_arr = list(set(arr))

    dict_arr = {}

    for i in set_arr:
        dict_arr[i] = arr.count(i)

    max_value = max(dict_arr.values())

    for key, value in dict_arr.items():
        if max_value == value:
            max_ids.append(key)

    return min(max_ids)
