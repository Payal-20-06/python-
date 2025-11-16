# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def show_menu():
    print("\n=========== Calculator App ===========")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("======================================")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Exiting... Goodbye! 👋")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Please select a number between 1–5.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    if choice == "1":
        print(f"Result: {add(num1, num2)}")
    elif choice == "2":
        print(f"Result: {subtract(num1, num2)}")
    elif choice == "3":
        print(f"Result: {multiply(num1, num2)}")
    elif choice == "4":
        print(f"Result: {divide(num1, num2)}")
