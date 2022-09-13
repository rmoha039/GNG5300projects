num1 = float(input("Input the first number: "))
num2 = float(input("Input the second number: "))

addition_result = num1 + num2
minus_result = num1 - num2
multi_result = num1 * num2
power_result = num1 ** num2

try:
    divi_result = num1/num2
except ZeroDivisionError as e:
    print("num2 can't be zero when num1 divide num2")
    divi_result = "infinity"

print("num1 + num2 =", addition_result)
print("num1 - num2 =", minus_result)
print("num1 * num2 =", multi_result)
print("num1 ** num2 =", power_result)
print("num1 / num2 =", divi_result)