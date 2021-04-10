#base case return one
#recursion case
"""
n!={
        1                    if n=0     #base case
        n.(n-1)!       if n>=1    #recursion case
}
"""

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

# for i in range(2,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i," This is prime")