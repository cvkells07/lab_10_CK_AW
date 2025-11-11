op = input("Enter the operation: ")
operand1 = float(input("Enter the first operand: "))
operand2 = float(input("Enter the second operand: "))
if op == "add":
    result = operand1 + operand2
elif op == "sub":
    result = operand1 - operand2
elif op == "mul":
    result = operand1 * operand2
elif op == "div":
    result = operand1 / operand2

if result%1 == 0:
    print(f"Result is {result:.1f}")
else:
    print(f"Result is {result:.2f}")