def compareTriplets(a, b):
    # Write your code here
    alice, bob = 0, 0
    
    for i, j in zip(a, b):
        if i > j:
            alice += 1
            
        if i < j:
            bob += 1
            
    return [alice, bob]

