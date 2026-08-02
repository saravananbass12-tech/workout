#Task:
#Write a program that asks the user for two numbers and divides them.
#If the user enters non-numeric input or divides by zero, handle the error gracefully.

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
    print("Result:", result)
    
except ValueError:
    print("Invalid input! Please enter numeric values.")
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
