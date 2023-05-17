if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list_arr = list(arr)
    list_arr.sort()
    max_arr = max(list_arr)
    
    for i in range(n-1, -1, -1):
        if list_arr[i] < max_arr:
            print(list_arr[i])
            break
