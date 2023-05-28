def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    apples_falls = 0
    oranges_falls = 0
    apples_with_a = []
    oranges_with_b = []

    for i in apples:
        apples_with_a.append(i+a)
        
    for j in oranges:
        oranges_with_b.append(j+b)
        
    for i in apples_with_a:
        if s <= i <= t:
            apples_falls += 1
            
    for j in oranges_with_b:
        if s <= j <= t:
            oranges_falls += 1
            
    print(apples_falls)
    print(oranges_falls)
