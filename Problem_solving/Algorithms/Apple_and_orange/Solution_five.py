def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    count_apples = 0
    count_oranges = 0
    
    for i in apples:
        if s <= i+a <= t:
            count_apples += 1
            
    for j in oranges:
        if s <= j+b <= t:
            count_oranges += 1
            
    print(count_apples)
    print(count_oranges)
