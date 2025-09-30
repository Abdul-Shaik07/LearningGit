

def reverse(a,rev):
    
    while a != 0:
        digit = a % 10
        rev = rev * 10 + digit
        a = a // 10
    print(rev)
reverse(111,0)