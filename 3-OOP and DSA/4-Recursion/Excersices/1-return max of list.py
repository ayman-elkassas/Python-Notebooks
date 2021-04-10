def maxreturn(list,start,stop,max=0):
    if len(list)<=1:
        return list[0]
    elif start>stop-1:
        return max
    else:
        if list[start]>=max:
            max=list[start]
            start+=1
            return maxreturn(list, start, stop, max)
        else:
            start+=1
            return maxreturn(list, start, stop, max)


list=[5,3,4,7,2]

data=[1]*8
print(data)
ma=maxreturn(list,0,len(list))
print(ma)
