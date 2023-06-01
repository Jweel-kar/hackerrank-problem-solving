def hurdleRace(k, height):
    # Write your code here

    max_value = max(height)
    
    if max_value > k:
        return int(max_value - k)
    
    elif max_value < k:
        return 0
