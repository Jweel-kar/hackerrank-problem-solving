def extraLongFactorials(n):
    # Write your code here
    
    result = 1
    
    for i in range(n, 1, -1):
        result *= i
        
    print(result)
