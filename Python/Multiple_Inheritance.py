
#Multiple_Inheritance  
#one child is having more than one parent
#While executing multiple_Inheritance, whenever we have same members of a class it gets confused. it always goes first left hand side.
 


class A():
    
    def name(self):
        print("My name is Shaik Abdul")
    
class B():
    
    def name(self):
        print("My age is 23")
        

class C(A,B):
    
    def height(self):
        print("My height is 5.9")


c = A()

b = B()

b.name()
c.name()