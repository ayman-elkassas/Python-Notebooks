# print(int.__doc__,int.__base__)
class A:
    i=123
    def __init__(self):
        self.i=123456

print(A.i)#class Attribute Defualt
print(A().i)#call constructor and assign value to i 