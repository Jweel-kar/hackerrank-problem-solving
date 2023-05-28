def timeConversion(s):
    # Write your code here

    zn = s[-2:]

    if zn == 'AM' and s[0:2] == '12':
        return '00' + s[2:-2]

    elif zn == 'PM' and s[:2] != '12':
        return str(int(s[0:2]) + 12) + s[2:-2]

    else:
        return s[:-2]
