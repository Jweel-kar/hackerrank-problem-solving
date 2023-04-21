from functools import reduce

def extraLongFactorials(n):
    # Write your code here
    
    print(reduce(lambda x, y: x*y, range(n+1)[1:]))
