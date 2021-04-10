class Access:
    f=5
    _s=4
    #class-level member access from class only and defualt to any object
    def __init__(self):
        self.a=5
        self.__b=6#private data
        self.f=7
    def __f(self):
        print("Welcome")
        print(self.__b)


access=Access()
access._Access__f()
print(access._Access__b)
# print(access.f)
#to access any private data ( Attribute or method ) should follow syntax :
# object._class__[private name]
# EX : access._Access__s()

