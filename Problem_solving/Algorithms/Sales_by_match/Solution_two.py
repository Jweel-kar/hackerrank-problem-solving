def sockMerchant(n, ar):
    # Write your code here
    
    pair = 0
    
    set_ar = list(set(ar))
    
    for i in set_ar:

        result = ar.count(i) // 2

        if result > 0:
            pair += result
            
    return pair

