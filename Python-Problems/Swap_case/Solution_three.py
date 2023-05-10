def swap_case(s):

    swap_s = ''
    
    for ch in s:

        if ch.isupper():
            swap_s += ch.lower()
            
        elif ch.islower():
            swap_s += ch.upper()
            
        else:
            swap_s += ch
            
    return swap_s
