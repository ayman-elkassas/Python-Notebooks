results=[]
def factor(n):
    for i in range(1,n+1):
        if n%i==0:
            results.append(i)
    return results
print(factor(100))
