def miniMaxSum(arr):
    # Write your code here
    arr.sort()

    mini = sum(arr[0:4])
    Max = sum(arr[1:])
    
    print(mini, Max)
