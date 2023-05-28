def timeConversion(s):
    # Write your code here

    if s[-2:] == 'AM':

        if s[0:2] == '12':
            s = '00' + s[2:-2]
            return s
        
        else:
            s = s[0:-2]
            return s
        
    elif s[-2:] == 'PM':
        
        if s[0:2] == '12':
            s = s[0:-2]
            return s
        
        else:
            s_one = int(s[0:2]) + 12
            s = str(s_one) + s[2:-2]
            return s
