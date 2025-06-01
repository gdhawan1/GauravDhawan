#task1

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Take input from user
num = int(input("Enter a number: "))

# Call the function and store result
fact = factorial(num)

# Print the result
print(f"Factorial of {num} is {fact}")

# task2

import math

num = float(input("Enter a number: "))

sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

print(f"Square root: {sqrt_val}")
print(f"Logarithm (base e): {log_val}")
print(f"Sine (radians): {sine_val}")


