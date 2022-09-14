num1 = float(input("Input the first number: "))
num2 = float(input("Input the second number: "))
operation = input("Input the operation(+, -, *, **, /): ")

operation_result = None
if operation == "+":
    operation_result = num1 + num2
elif operation == "-":
    operation_result = num1 - num2
elif operation == "*":
    operation_result = num1 * num2
elif operation == "**":
    operation_result = num1 ** num2
elif operation == "/":
    try:
        divi_result = num1 / num2
    except ZeroDivisionError as e:
        print("num2 can't be zero when num1 divide num2")
        operation_result = "infinity"
else:
    print("no such operation")

print("The equation result is: ", operation_result)

# Addition by Rasheeq Mohammad
num3 = float(input("Input the third number: "))

if operation == "+":
    operation_result = operation_result + num3
elif operation == "-":
    operation_result = operation_result - num3
elif operation == "*":
    operation_result = operation_result * num3
elif operation == "**":
    operation_result = operation_result ** num3
elif operation == "/":
    try:
        divi_result = operation_result / num3
    except ZeroDivisionError as e:
        operation_result = "infinity"
else:
    print("no such operation")

print("The equation result is: ", operation_result)
