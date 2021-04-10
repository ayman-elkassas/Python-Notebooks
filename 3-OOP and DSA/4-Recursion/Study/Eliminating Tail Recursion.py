# Eliminating Tail Recursion
def binary_search(target,list):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        if target==list[mid]:
            return True
        elif target <list[mid]:
            high=mid-1
        else:
            low=mid+1
    return False

list=[1,4,5,6,7]
print(binary_search(5,list))
