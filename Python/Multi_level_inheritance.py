
class A:
    def __init__(self,land,area):
        self.__land = land
        self.area = area
        
    def get_land(self):
        return self.__land
    
class B(A):
    def __init__(self, land, area,house):
        super().__init__(land, area)
        self.house = house
        
class C(B):
    
    def __init__(self, land, area, house):
        super().__init__(land, area, house)
    
    def print(self):
        print(f"land is {self.get_land()}, area is {self.area} and house is near {self.house}")
        
    
c = C('2 acres','Y Kota','Lakshmi Paradise')

c.print()