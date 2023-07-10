def serviceLane(n, cases):
    # Write your code here

    segments = []

    for case in cases:

        width_list = []

        for lane in range(case[0], case[1]+1):
            width_list.append(width[lane])

        segments.append(min(width_list))
        
    return segments

