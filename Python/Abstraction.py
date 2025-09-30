
from abc import ABC,abstractmethod

class A():
    
    @abstractmethod
    def hi(self):
        pass
    def hello(self):
        print("normal method hello() - hello")

class B():
    
    @abstractmethod
    def h(self):
        pass
        
    def i(self):
        print("normal method i() - i")
        

class C(A):
    
    def hi(self):
        print("override hi method from abstrcat method in class A - hi")
        
    def hello(self):
        print("override hello method from normal method in class A - hello")

class D(B):

    def h(self):
        print("override h method from abstrcat method in class B - h")
    
    def i(self):
        print("override i method from normal method in class B - i")



c = C()
c.hi()
c.hello()

d = D()
d.h()
d.i()



a = A()
a.hello()
a.hi()

b = B()
b.i()
b.h()