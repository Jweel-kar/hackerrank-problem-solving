def utopianTree(n):
    # Write your code here

    height = 0
    
    for i in range(n+1):

        if i == 0 or i % 2 == 0:
            height += 1
    
        elif i % 2 != 0:
            height *= 2
    
    return height

