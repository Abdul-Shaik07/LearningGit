"""file = open("practice.txt","w")
file.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")"""

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")

print(f.read())