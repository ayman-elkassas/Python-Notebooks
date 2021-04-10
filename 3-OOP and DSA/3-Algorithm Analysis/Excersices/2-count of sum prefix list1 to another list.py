def countTotal(ls,B):
    n=len(ls)
    count=0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1+j):
                total+=ls[k]
        if total==B[i]:
            count+=1
    return count

ls=[0,1,1,77,1,1]
B=[49,2,0,4,44,1]
print(countTotal(ls,B))