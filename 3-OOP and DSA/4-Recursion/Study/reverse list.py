def reverse(list,start,stop):
    if start <stop-1:
        list[start],list[stop-1]=list[stop-1],list[start]
        reverse(list,start+1,stop-1)

list=[1,2,3,4,5]
reverse(list,0,len(list))
print(list)
# print(pow(2,4))