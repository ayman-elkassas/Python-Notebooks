def productOdd(n):
    for i in range(0,len(n)):
        for j in range(1,len(n)):
            if n[i]*n[j]%2!=0:
                printNumbers(n[i],n[j])
        break

def printNumbers(x,y):
    print(x,y,"And product = ",x*y)

s=[5,2,7,3,6]
productOdd(s)