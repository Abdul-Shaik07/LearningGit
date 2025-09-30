


f = open('movie','r')

f1 = open('data','a')

for content in f:
    print(f1.write(content))