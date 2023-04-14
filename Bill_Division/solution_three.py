def bonAppetit(bill, k, b):
    # Write your code here
    
    bill_actual = (sum(bill) - bill[k]) // 2
    
    if bill_actual == b:
        print('Bon Appetit')
        
    else:
        print(b - bill_actual)
