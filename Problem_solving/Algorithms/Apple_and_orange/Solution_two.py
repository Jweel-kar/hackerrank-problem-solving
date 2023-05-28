def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    apples_falls = 0
    oranges_falls = 0
        
    for i in apples:
        if s <= i+a <= t:
            apples_falls += 1
            
    for j in oranges:
        if s <= j+b <= t:
            oranges_falls += 1
            
    print(apples_falls)
    print(oranges_falls)
