class flower:
    _name=""
    _price=0
    _numofpelate=0.0

    def __init__(self,name,price,numofpelate):
        self._name=name
        self._price=price
        self._numofpelate=numofpelate

    def setname(self,name):
        self._name=name
    def setprice(self,price):
        self._price=price
    def setnumofplate(self,numofpelate):
        self._numofpelate=numofpelate

    def getname(self):
        return  self._name
    def getprice(self):
        return self._price
    def getnumofpalet(self):
        return self._numofpelate


