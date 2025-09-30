'''

a = "5"

b = "10"

c = int(b)

d = 23

e = (d)

print(e, type(e))

print(b, type(b))

print(c, "and type is", type(c))

print(int(a) * int(b))


multiplication = 17
i=1

while(i < 11):
    print(multiplication, "*", i, "=", multiplication*i)
    i += 1
print(multiplication)

'''
'''

# Prime Number
primeNumber = 5
if primeNumber > 1:
    for i in range(2, (primeNumber//2) + 1):
        if (primeNumber % i) == 0:
            print(primeNumber, "is not a prime number")
            break
        else:
            print(primeNumber, "is a prime number")
else:
    print(primeNumber, "is not a prime number")       


'''
'''

palindrome = 12
temp = palindrome
rev = 0
while palindrome != 0:
    digit = palindrome % 10
    rev = rev * 10 + digit
    palindrome = palindrome // 10
    
print(rev)

if temp == rev:
    print("palindrome")
else:
    print("not a palindrome")
    
'''
'''

fact = 1
n = 5
while n != 0:
    fact = fact * n
    n -= 1
print(fact)

'''
'''

armstrong = 70
power = 0
temp = armstrong
while armstrong != 0:
    digit = armstrong % 10
    power = power + digit ** 3
    armstrong = armstrong // 10
    
if(temp == power):
    print(temp, "is an Armstrong number")
else:
    print(temp, "is not an Armstrong number")
    
print(power)
print(digit)
print(armstrong)
        
'''

'''

n = 4
for i in range(n+1): 
    for j in range(1, n-i+1):
       print(j, end = " ")
    print()    
    
'''

'''

a = 0
b = 1
n = 10
print(a)
print(b)
for i in range(n):
    c = a + b
    a = b
    b = c
    
    print(c)
    
'''
'''

list = [10,20,30,40,10]
l = [] 

for a in list:
    if a not in l:
        l.append(a)
    print(a)
print(l)
print(list)

'''

'''
n = 1023456782431
evenCount = 0
oddCount = 0
while n != 0:
    digit = n % 10;
    if digit % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
    n = n // 10
print("Even count in the number is", evenCount)
print("Odd count in the number is", oddCount)
print(n)
'''
from abc import abstractmethod


@abstractmethod
class Test():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @abstractmethod
    def print(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
class Exam(Test):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def printDetails(self):
        print(self.name, self.age, self.subject)
    

myTest = Test("Abdul", 24)
myTest.print()

myExam = Exam("Abdul", 24, "Python")
myExam.printDetails()