class Animal:
    def name(self):
        pass
    def sleep(self):
        print("go to sleep")
    def makenoise(self):
        pass

class dog(Animal):
    def name(self):
        print("my name is dog")
    def makenoise(self):
        print("hooooooooo")

class test:
    def s(self,Animal):
        Animal.name()
        Animal.makenoise()
t=test()
d=dog()
t.s(d)
#polymorophism is used when you don't know type of parameter passing
def s(object):
    print(object.__doc__)

s(int)












































