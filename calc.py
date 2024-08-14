# Simple calculator 

def add(x,y):
    return x + y 
def sub(x,y):
    return x - y
def mul(x,y):
    return x*y
def div(x,y):
    if y != 0:
        return x/y
    else: 
        return "Cannot divide by zero"
        
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

if choice == '1':
    print(f"Your output is : {add(num1,num2)}")
elif choice == '2':
    print(f"Your output is : {sub(num1,num2)}")
elif choice == '3':
    print(f"Your output is: {mul(num1,num2)}")
elif choice == '4':
    print(f"Your output is: {div(num1,num2)}")
else:
    print("Invalid input")
