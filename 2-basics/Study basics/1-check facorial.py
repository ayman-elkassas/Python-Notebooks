from math import factorial

fact=0
def  is_multiple(n, m):
    fact=factorial(n)
    if fact == m:
        return True
    else:
        return False


print(is_multiple(3,6))

