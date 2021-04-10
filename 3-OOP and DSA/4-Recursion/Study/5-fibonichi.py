# Fn
# = F
# n−2 + Fn−1 for n > 1.
# import gzip
# gzip.GzipFile.readline(r"C:\Users\Ayman Elkassas\Desktop\dump.txt",)
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(5))
