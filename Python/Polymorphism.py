
#MethodOverriding

class A():
    
    def a(self):
        a = 10
        b = 20
        print(a+b)

class B(A):
    
    def a(self):
        a = 20
        b = 20
        print(a+b)


b = B()

b.a()


