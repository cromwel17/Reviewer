num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

sum = num1 + num2
subtraction = num1 - num2
divide = num1 / num2
multiply = num1 * num2

total = f"The {num1} {operator} {num2} is {sum}"

print(total)

