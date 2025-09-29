#Calculator (exersice -1)
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Can't divide by zero."
    return x / y

print("select operation:")
print("1.add")
print("2.subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

if choice == "1":
    print("Result:", add(num1,num2))
elif choice == "2":
    print("Result:", subtract(num1,num2))
elif choice == "3":
    print("Result:", multiply(num1,num2))
elif choice == "4":
    print("Result:", divide(num1,num2))
else:
    print("Invalid input!")
