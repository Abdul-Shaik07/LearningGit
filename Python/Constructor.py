
class Construct():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def print(self):
        print(f"my name is {self.name}, age is {self.age} and gender is {self.gender}")
        
        
c = Construct('Abbu',23,'M')
c.print()
c.hello()