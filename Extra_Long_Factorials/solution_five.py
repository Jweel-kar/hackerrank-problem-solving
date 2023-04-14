def extraLongFactorials(n):
    # Write your code here
    
    def fact(n):
        if (n == 1):
            return 1
            
        prod = n * fact(n - 1)
        return prod
        
    print(fact(n))
