def catAndMouse(x, y, z):
    
    dis_A = abs(z - x)
    dis_B = abs(z - y)
    
    if dis_A < dis_B:
        return 'Cat A'
    
    elif dis_B < dis_A:
        return 'Cat B'
    
    else:
        return 'Mouse C'
