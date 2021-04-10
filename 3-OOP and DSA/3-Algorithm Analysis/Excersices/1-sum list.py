def sum(lis):
    n=len(lis)
    total=0
    for i in range(0,n):
        total+=lis[i]
    return total

ls=[1,2,3,4,5]
print(sum(ls))