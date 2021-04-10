def numofdiv(n,count):
    if n<=2:
        return count
    else:
        return numofdiv(n / 2,count+1)
print(numofdiv(20,0))