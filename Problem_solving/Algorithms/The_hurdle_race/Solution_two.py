def hurdleRace(k, height):
    # Write your code here
    
    max_height = max(height)
    
    if max_height > k:
        return max_height - k
    
    else:
        return 0
