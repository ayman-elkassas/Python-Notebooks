def binaryRecursion(list,start,stop):
    if start>stop-1:
        return 0
    elif start==stop-1:
        return list[start]
    else:
        mid=int((start+stop)//2)
        return binaryRecursion(list,start,mid)+binaryRecursion(list,mid,stop)

list=[1,2,3,5,22]
print(binaryRecursion(list,0,len(list)))