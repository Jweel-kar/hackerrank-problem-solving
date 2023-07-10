def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #

    costs = []
    
    for i in keyboards:
        for j in drives:

            cost = i + j

            if cost <= b:
                costs.append(cost)

    if 0 < len(costs):
        return max(costs)

    else:
        return -1

