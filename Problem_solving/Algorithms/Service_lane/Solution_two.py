def serviceLane(n, cases):
    # Write your code here

    max_width = []
    
    for i in cases:
        max_width.append(min(width[i[0]: i[-1] + 1]))

    return max_width

