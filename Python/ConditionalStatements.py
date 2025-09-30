#we have 4 conditional statements which consists of 
#if - else, elif, and nested if.

a = int(input("enter the 1st number : "))

b = int(input("enter the 2nd number : "))

c = int(input("enter the 3rd number : "))

if a > b and a > c:
    print("a is bigger than b")
elif b > c:
    print("b is bigger than c")
else:
    print("c is bigger than a and b")
    
#nestedIf
if a >= b:
    if a == b:
        print(a)
    print("Good peoples comes in our life, if we are good")
else:
    print("Don't hurt to anyone")
    
#Switch as match 

n = input("enter the string : ")

match n:
    case 'abdul':
        print(0)
    case 'abbu':
        print(1)
    case 'ayesha':
        print(2)
    case 'aira':
        print(3)
    case _:
        print('bye')    
    
