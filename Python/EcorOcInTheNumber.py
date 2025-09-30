
n = int(input("Enter the number : "))
ec = 0
oc = 0
while n != 0:
    if n % 2 == 0:
        ec += 1
    else:
        oc += 1
    n = n // 10 
print(ec)
print(oc)
        