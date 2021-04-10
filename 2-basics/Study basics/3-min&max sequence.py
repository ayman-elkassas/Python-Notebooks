def maxmin(n):
    """
    :param n:
    :return:  maxs,mins list
    """
    i=0
    maxs = n[i]
    mins=n[i]
    for i in n:
        if i>maxs:
            maxs = i
        if i < mins:
            mins = i
    return maxs,mins

s=[25,1,7,9,20]
print(maxmin(s))



