num1=float(input("Enter the First Number : "))
num2=float(input("Enter the First Number : "))
operation = input("Choose the operation (+, -, *, /, ^): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
elif operation == '^':
    result = num1 ** num2
else:
    print("Invalid Input")
print(result)