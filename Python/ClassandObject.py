class A0():
    def __init__(self, Ename, Eid):
        self.__Ename = Ename
        self.Eid = Eid
    def data(self):
        return self.Eid, self.__Ename
    
a = A0("Abdul",1)
print(a.data())
