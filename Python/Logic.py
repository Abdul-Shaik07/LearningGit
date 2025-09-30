'''
# Reverse a number
def reverse_num(num,rev):
    print("Before reversing is",num)
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit 
        num //= 10
    return rev
print("After reversing is", reverse_num(23,0))
'''

'''         
# Fibonacci Series
def fibonacci(a, b, n):
    print(a)
    print(b)
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
        print(c)
fibonacci(0, 1, 10)
'''

'''
# Palindrome or not
def palindrome(n, rev):
    temp = n
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if temp == rev:
        return "palindrome"
    else:
        return "not a palindrome"
print(palindrome(22, 0))
'''

# pattern programs
''''
def A(n):                           
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
A(5)
'''

'''
def A(n):
    for i in range(1, n+1):
        for j in range(n):
            print(i, end=" ")
        print() 
A(5)               
'''

'''
def A(n):
    for i in range(1, n+1):
        for j in range(1,n+1):
            print(j, end=" ")
        print() 
A(5)  
'''

'''
def A(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
A(5)
'''

