def migratoryBirds(arr):
    # Write your code here

    max_ids = []

    dict_arr = {}

    for i in arr:
        if i not in dict_arr:
            dict_arr[i] = 1
            
        else:
            dict_arr[i] += 1

    max_value = list(dict_arr.values())[0]
    
    for i in dict_arr.values():
        if max_value < i:
            max_value = i

    for key, value in dict_arr.items():
        if max_value == value:
            max_ids.append(key)

    min_id = max_ids[0]
    
    for i in max_ids:
        if i < min_id:
            min_id = i
            
    return min_id

