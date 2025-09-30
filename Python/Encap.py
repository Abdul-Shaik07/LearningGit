class Encap():
    def __init__(self,name,age):
        self.__name = name
        self.age = age
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def printa(self):
        print(self.get_name())
       
    
e = Encap("Abdul",23)
e.set_name("Abbu")
e.printa()
