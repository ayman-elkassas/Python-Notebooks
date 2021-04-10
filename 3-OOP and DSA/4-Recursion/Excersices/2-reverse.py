def reverse(list,start,stop):
    if start>=stop:
        return list
    else:
        list[start],list[stop-1]=list[stop-1],list[start]
        start,stop=start+1,stop-1
        return reverse(list,start,stop)

list=[1,2,3,4]
revlist=reverse(list,0,len(list))
print(revlist)
