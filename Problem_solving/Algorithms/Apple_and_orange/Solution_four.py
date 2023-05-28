def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    count_apples = 0
    count_oranges = 0
    
    for i in apples:
        if i+a in range(s, t+1):
            count_apples += 1
            
    for j in oranges:
        if j+b in range(s, t+1):
            count_oranges += 1
            
    print(count_apples)
    print(count_oranges)
