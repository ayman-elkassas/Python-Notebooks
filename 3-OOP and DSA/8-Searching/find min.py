def searchonmin(listmin):
    min = listmin[0]
    for i in range(len(listmin)-1):
        if min>listmin[i+1]:
            min=listmin[i+1]
    return min

list=[10,5,2,8,7]
min=searchonmin(list)
print(min)