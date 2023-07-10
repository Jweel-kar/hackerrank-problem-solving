def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #

    price = []
    count = 0
    
    for i in keyboards:
        for j in drives:

            if (i + j) <= b:
                price.append(i+j)
                count += 1
                
    if count > 0:
        max_price = price[0]
        
        for i in price[1:]:
            if i > max_price:
                max_price = i
                
        return max_price
    
    else:
        return -1

