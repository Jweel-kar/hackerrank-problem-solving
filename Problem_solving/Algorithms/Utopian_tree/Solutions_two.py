def utopianTree(n):
    # Write your code here
    
    growth = {}

    for i in range(1, 60):

        growth[0] = 1

        if i % 2 != 0:
            growth[i] = growth[i-1] * 2

        else:
            growth[i] = growth[i-1] + 1

    return growth[n]

