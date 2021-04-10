import math
def sumSmallSquares(n):
    """
    :param n:
    :return:sum of small squares
    """
    result=0
    for i in range(1,n):
        if i%2==0:
            continue
        else:
            result=result+math.pow(i,2)

    return result

print(sumSmallSquares(6))