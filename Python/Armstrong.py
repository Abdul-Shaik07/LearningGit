n = 153
temp = n
rev = 0
while n != 0:
    digit = n % 10
    rev = rev + digit ** 3
    n = n // 10
if temp == rev:
    print(temp, "is a armstrong")
else:
    print(temp, "is not a armstrong")
