
class Encap:
                                        
    __name = 'Abdul'                    #By using normal of getter() amd setter()
    __age = 23
    
    '''
    def __init__(self,name,age):
        self.__name = name              #By using constructor of getter() and setter()
        self.__age = age
    '''
    
    
    def get_name(self):
        return self.__name    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
     
    def print(self):
        print(self.get_name(), self.get_age())
     
        
e = Encap()
e.print()
# print(e.get_name())
# print(e.get_age())


