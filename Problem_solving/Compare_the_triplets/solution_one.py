def compareTriplets(a, b):
    # Write your code here
    alice_point = 0
    bob_point = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                if a[i] > b[j]:
                    alice_point += 1
                elif a[i] < b[j]:
                    bob_point += 1
                elif a[i] == b[j]:
                    pass
    return [alice_point, bob_point]
