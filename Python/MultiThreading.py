
from threading import *
from time import sleep

class A(Thread):
    
    def run(self):
         i = 0
         while i < 10:
             print(i)
             i += 1
             sleep(0.2)
             

class B(Thread):
    
    def run(self):
        for i in range(10):
            print("the value of i is ",i)
            sleep(0.2)
 
 
a = A()
b = B()
 
a.start()
b.start()

a.join()
b.join()
print('bye')
