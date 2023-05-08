def miniMaxSum(arr):
    # Write your code here
    arr_sum = 0
    arr_min = arr[0]
    arr_max = arr[0]

    for i in arr:
        arr_sum += i

        if i < arr_min:
            arr_min = i

        if i > arr_max:
            arr_max = i

    print(arr_sum - arr_max, arr_sum - arr_min)

