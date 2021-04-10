def binarysearch(listitem,item):
    low=0
    high=len(listitem)-1
    while low<=high:
        mid=(high+low)//2
        if listitem[mid] == item:
            return True
        elif listitem[mid]>item:
            high=mid-1
        else:
            low=mid+1
    return False

list=[5,1,2,7,10]
listsort=sorted(list)
flag=binarysearch(listsort,5)
print(flag)