class stack:
    """
    This is class stack for operations stack
    push,pop,top,is_empty,len
    """
    def __init__(self):
        self._data = []

    def push(self,e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Exception("Empty stack")
        return self._data.pop()
    def top(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data)==0

    def __len__(self):
        return len(self._data)
"""
usage:
    s=stack()
    s.push(5)
    s.push(6)
    print(len(s))
    s.pop()
    print(len(s))
    s.push(66)
    print(s.top())
    s.pop()
    s.pop()
    print(len(s))
"""
