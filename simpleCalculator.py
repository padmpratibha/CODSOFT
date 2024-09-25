def add(v1,v2):
    return v1+v2

def sub(v1,v2):
    return v1-v2

def mult(v1,v2):
    return v1*v2

def division(v1,v2):
    return v1/v2

def mod(v1,v2):
    return v1%v2

def floordiv(v1,v2):
    return v1//v2

# def inverse(v1,v2):
#     return -v1,-v2

print("------WELCOME-----")
val1 = int(input("enter first value : "))
val2 = int(input("enter second value : "))

while True:
        
    print(f"""
        1. Addition 
        2. Substraction
        3. Division
        4. Multiplication
        5. Mod Division
        6. Percentage
        
        
        """)

    Choice = int(input("enter your choice : "))

    if Choice == 1:
        print(add(val1,val2))
    elif Choice == 2:
        print(sub(val1,val2))
    elif Choice == 3:
        print(division(val1,val2))
    elif Choice == 4:
        print(mult(val1,val2))
    elif Choice == 5:
        print(mod(val1,val2))
    elif Choice == 6:
        print(floordiv(val1,val2))
    else:
        print("Wrong Input.......")
        break

print("--------Thankyou-------")





