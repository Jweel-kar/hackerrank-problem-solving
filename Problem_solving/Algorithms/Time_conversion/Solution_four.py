def timeConversion(s):
    # Write your code here

    if s[-2:] == 'AM' and int(s[:2]) == 12:
        return '00' + s[2:-2]
                
    if s[-2:] == 'PM' and int(s[:2]) != 12:
        return str(int(s[:2]) + 12) + s[2:-2]
        
    else:
        return s[:-2]
