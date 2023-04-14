def bonAppetit(bill, k, b):
    # Write your code here
    
    b_actual = 0

    for i in range(len(bill)):
        if i != k:
            b_actual += bill[i]
            
    half = b_actual / 2
    
    if b == half:
        print('Bon Appetit')
    
    else:
        print(int(b - half))
