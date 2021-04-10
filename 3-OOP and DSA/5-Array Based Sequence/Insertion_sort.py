#INSERTION SORT
def insertion_sort(list):
    for i in range(1,len(list)):
        cur=list[i]
        j=i
        while j>0 and list[j-1]>cur:
            list[j]=list[j-1]
            j-=1
        list[j]=cur

list=[1,8,6,3,2]
insertion_sort(list)
print(list)
