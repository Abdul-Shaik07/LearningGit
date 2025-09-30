
class Product():
    
    def __init__(self, n, p, pri):
        self.name = n
        self.pid = p
        self.price = pri
        
class Mobile(Product):
    
    def __init__(self, n, p, pri,r):
        super().__init__(n, p, pri)
        self.ram = r
        
    def mobile_Data(self):
        print(f"name is {self.name}, proudct_Id is {self.pid}, price is {self.price}, and ram is {self.ram}")
        
class PowerBank(Product):
    
    def __init__(self, n, p, pri,m):
        super().__init__(n, p, pri)
        self.mah = m
        
    def PowerBank_Data(self):
        print(f"name is {self.name}, proudct_Id is {self.pid}, price is {self.price}, and ram is {self.mah}")
    
class Shirt(Product):
    def __init__(self, n, p, pri,s):
        super().__init__(n, p, pri)
        self.size = s
        
    def Shirt_Data(self):
        print(f"name is {self.name}, proudct_Id is {self.pid}, price is {self.price}, and ram is {self.size}")
        
    

mobile = Mobile('Shaik', 24803, 999.67, '6GB') 
mobile.mobile_Data()      

powerbank = PowerBank('Abbu',24804, 1456.78, '10000mah')
powerbank.PowerBank_Data()

shirt = Shirt('Abdul', 24803, 589.87, 'XL')
shirt.Shirt_Data()