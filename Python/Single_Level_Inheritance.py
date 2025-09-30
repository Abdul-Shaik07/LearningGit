
class A:
    def __init__(self, name):
        self.name = name
        print("hello")
    
    def print(self):
        print(f"my name is {self.name} and I live in Tirupati")
    
    

class B(A):
    def __init__(self, name, age):
        super().__init__(name)
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def print1(self):
        print(f"my name is {self.name}, my age is {self.get_age()} and later on I moved to Bangalore")
    
    

b = B('Abdul',23)

b.print()
b.print1()