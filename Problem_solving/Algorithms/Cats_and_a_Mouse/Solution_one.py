def catAndMouse(x, y, z):

    dis_A = abs(z - x)
    dis_B = abs(z - y)
    
    if dis_A > dis_B:
        return 'Cat B'
        
    elif dis_A < dis_B:
        return 'Cat A'
        
    elif dis_A == dis_B:
        return 'Mouse C'
