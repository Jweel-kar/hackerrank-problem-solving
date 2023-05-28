def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    apples_plus = []
    oranges_plus = []
    count_apples = 0
    count_oranges = 0
    
    for i in apples:
        apples_plus.append(i+a)
        
    for j in oranges:
        oranges_plus.append(j+b)
        
    for k in apples_plus:
        if k in range(s, t+1):
            count_apples += 1
            
    for l in oranges_plus:
        if l in range(s, t+1):
            count_oranges += 1
            
    print(count_apples)
    print(count_oranges)
