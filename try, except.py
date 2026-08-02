#Task 1: Simple division with error handling

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter numeric values.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")



#Task 2: Multiple exceptions in one except


try:
    n = int(input("Enter an integer: "))
    print("You entered:", n)
except (ValueError, TypeError):
    print("Invalid input! Please enter a valid integer.")
except Exception as e:
    print("An unexpected error occurred:", e)


#Task 3: Using else and finally

try:
    n = float(input("Enter a number: "))
    square = n ** 2
except (ValueError, TypeError):
    print("Invalid number!")
else:
    print("Square:", square)
finally:
    print("Execution complete.")



#Task 4: File handling with exceptions


try:
    with open("data.txt", "r") as f:
        content = f.read()
    print("File content:\n", content)
except FileNotFoundError:
    print("Error: File 'data.txt' not found.")
except IOError as e:
    print("Error reading file:", e)


#Task 5: Custom exception

class NegativeNumberError(Exception):
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Number cannot be negative!")
    return n

try:
    num = float(input("Enter a positive number: "))
    check_positive(num)
    print("Valid positive number:", num)
except NegativeNumberError as e:
    print("Custom error:", e)
except ValueError:
    print("Invalid input! Please enter a numeric value.")











    
