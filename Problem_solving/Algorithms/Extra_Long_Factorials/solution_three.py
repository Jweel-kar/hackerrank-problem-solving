def extraLongFactorials(n):
    # Write your code here
    
    result = 1
    
    for i in range(1, n+1):
        result *= i
        
    print(result)
