def bonAppetit(bill, k, b):
    # Write your code here
    
    bill_without_k = 0
    
    for i in range(len(bill)):
        if i != k:
            bill_without_k += bill[i]
    
    bill_actual = bill_without_k // 2
    
    if b == bill_actual:
        print('Bon Appetit')
        
    else:
        print(b - bill_actual)
