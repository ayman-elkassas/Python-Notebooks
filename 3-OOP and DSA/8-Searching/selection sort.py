def selectiosort(list):
    n=len(list)
    for i in range(n-1):
        smallindex=i
        for j in range(i+1,n):
            if list[smallindex]>list[j]:
                smallindex=j
    list[smallindex],list[i]=list[i],list[smallindex]

list=[2,0,1,5,7]
selectiosort(list)
print(list)



