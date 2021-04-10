def bubbleSort(list):
    n=len(list)
    for i in range(n-1):
        for j in range(n-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]

list=[5,1,7,2,0,8]
bubbleSort(list)
print(list)