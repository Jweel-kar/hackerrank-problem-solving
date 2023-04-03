def miniMaxSum(arr):
    # Write your code here
    n = 5
    add_list = []

    for i in range(n):
        res = 0
        for j in range(n):
            if i != j:
                res += arr[j]
        add_list.append(res)

    print(min(add_list), max(add_list))
