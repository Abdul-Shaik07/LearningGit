'''
def pattern(n):
    for i in range(n):
        for j in range(n - i):
            print(' ',end = '')
        for j in range(i + 1):
            print('A',end = ' ')
        print()
pattern(5)

'''
"""

def pattern(n):
    
    for i in range(n):
       
        for j in range(n - i):
            print(' ',end = '')

        for j in range(i + 1):
            print('*', end = ' ')
        print()

pattern(5) 

"""


'''
def pattern(n):
    
    for i in range(n):
        
        for j in range(1, i + 2):
            print(j, end=' ')
        print()
        
pattern(5)

'''

'''

def pattern(n):
    
    for i in range(n):
        
        for j in range(i + 1):
            print(' ',end = ' ')
            
        for j in range(n - i):
            print('*',end = ' ')
            
        print()

pattern(5)

'''


"""

def pattern(n):
    
    for i in range(n):
        
        for j in range(n - i):
            
            print(' ',end = ' ')
        
        for j in range(i + 1):
            print("*", end= ' ')
        print()

pattern(5)

"""

"""

def pattern(n):
    
    for i in range(n):
        for j in range(n - i):
            print("*", end= " ")
        print()
pattern(5)


"""





"""

def pattern(n):
    
    for i in range(1,n):
        
        for j in range(i + 0):
            
            print(i, end= " ")
            
        print()
        
pattern(6)

"""        

"""

def pattern(n):
    
    for i in range(n):
        
        for j in range(n - i):
            
            print("*", end= " ")
        
        print()
        
pattern(5)

"""

"""

def pattern(n = 5):
    
    for i in range(0,n):
        
        for j in range(i + 1):
            
            print("*", end= " ")
        print()

pattern()

"""



def pattern(n):
    
    for i in range(1,n - 2):
        
        for j in range(1,n):
            
            print(i, end=" ")
        print()      
pattern(6)


"""

def pattern(n):
    
    for i in range(n - 3):
        
        for j in range(1, n):
            
            print(j, end=" ")

        print()
pattern(6)

"""


"""

def pattern(n):
    
    for i in range(0,n):
        
        for j in range(0,n):
            
            print("*", end=" ")
            
        print()
        
pattern(5)

"""