def sumFirstN(list,n):
    if n == 0:
        return 0
    else:
        return sumFirstN(list,n-1)+list[n-1]

list=[3,5,1,12]
print(sumFirstN(list,1))