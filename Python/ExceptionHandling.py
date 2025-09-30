from time import *
def exception():
    try:
        a = 5
        b = 2
        print(a/b)
        sleep(10)
        try:
            str = "Abdul"
            print(str[5])
            sleep(10)
        except IndexError as i:
            print("index error", {i})
    except ValueError as v:
        print("value error", {v})
        
    finally:
        sleep(30)
        print("Finally block executed")

sleep(20)
print("Exception Handling")
        
exception()
        
