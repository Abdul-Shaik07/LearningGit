
from array import *
arr = array('i',[0,1,2,3,4])
b = arr.__len__()
print(b)

arr1 = array('f',[12.4,5.67,2.34])
for i in arr1:
    print(i)
    

arr2 = array('u',['A','b','b','u'])
print(arr2.index('b'))
print(arr2.count('b'))
print(arr2.append('s'))
print(arr2)



"""
iterator = 0
while iterator < len(arr):
    iterator += 1 
print(iterator)

"""