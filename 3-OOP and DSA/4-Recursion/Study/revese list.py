def revese(list):
    start,stop=0,len(list)-1
    while start<stop:
        list[start],list[stop]=list[stop],list[start]
        start,stop=start+1,stop-1

list=[1,5,7,6,4]
revese(list)
print(list)