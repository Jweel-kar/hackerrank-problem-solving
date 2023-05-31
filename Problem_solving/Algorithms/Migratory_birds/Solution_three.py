def migratoryBirds(arr):
    # Write your code here

    max_ids = []

    dict_arr = {}

    for i in arr:
        if i not in dict_arr:
            dict_arr[i] = 1
            
        else:
            dict_arr[i] += 1

    max_value = max(dict_arr.values())

    for key, value in dict_arr.items():
        if max_value == value:
            max_ids.append(key)

    return min(max_ids)

