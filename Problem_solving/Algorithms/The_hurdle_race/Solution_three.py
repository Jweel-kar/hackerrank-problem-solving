def hurdleRace(k, height):
    # Write your code here
    
    max_height = height[0]
    
    for i in height:
        if i > max_height:
            max_height = i
    
    if max_height > k:
        return max_height - k
    
    else:
        return 0
