def binarySearch(target,list,max,min):
    mid=int((max+min)/2)
    if target==list[mid]:
        return True
    if min>=max:
        return False

    elif target >list[mid]:
        return binarySearch(target,list,max,mid+1)
    else:
        return binarySearch(target,list,mid-1,min)

list=sorted([1,2,3,10,6,5])
# print(sorted(list))
print(binarySearch(5,list,len(list)-1,0))
