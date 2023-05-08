def birthday(s, d, m):
    # Write your code here

    count = 0

    for i in range(len(s)):
        if (i+m) <= len(s):
            if len(s[i:i+m]) == m and sum(s[i:i+m]) == d:
                count += 1

    return count
