'''#================================================================================
                    PYTHON FUNCTIONS - COMPLETE GUIDE
#================================================================================

TABLE OF CONTENTS:
1. Basic Function Definition
2. Function with Multiple Parameters
3. Return Multiple Values
4. *args (Variable Positional Arguments)
5. **kwargs (Variable Keyword Arguments)
6. Lambda Functions (Anonymous)
7. Map Function
8. Filter Function
9. Reduce Function
10. Zip Function
11. Enumerate Function
12. Higher-Order Functions
13. Closures (Nested Functions)
14. Decorators
15. Recursive Functions
16. Type Hints (Modern Python)

================================================================================

1. BASIC FUNCTION DEFINITION
--------------------------------------------------------------------------------
def greet(name):
    """This function greets the user"""
    return f"Hello, {name}!"

# Call the function
result = greet("Saravanan")
print(result)  # Output: Hello, Saravanan!

================================================================================

2. FUNCTION WITH MULTIPLE PARAMETERS
--------------------------------------------------------------------------------
def add_numbers(a, b, c=0):
    """Add two or three numbers"""
    return a + b + c

print(add_numbers(5, 3))        # Output: 8
print(add_numbers(5, 3, 2))     # Output: 10

================================================================================

3. RETURN MULTIPLE VALUES
--------------------------------------------------------------------------------
def calculate(a, b):
    """Return sum, difference, and product"""
    sum_val = a + b
    diff = a - b
    product = a * b
    return sum_val, diff, product

s, d, p = calculate(10, 5)
print(f"Sum: {s}, Diff: {d}, Product: {p}")
# Output: Sum: 15, Diff: 5, Product: 50

================================================================================

4. *ARGS (VARIABLE POSITIONAL ARGUMENTS)
--------------------------------------------------------------------------------
def sum_all(*args):
    """Sum any number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))          # Output: 6
print(sum_all(1, 2, 3, 4, 5))    # Output: 15

================================================================================

5. **KWARGS (VARIABLE KEYWORD ARGUMENTS)
--------------------------------------------------------------------------------
def print_details(**kwargs):
    """Print key-value pairs"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Saravanan", age=25, city="Vellore")
# Output:
# name: Saravanan
# age: 25
# city: Vellore

================================================================================

6. LAMBDA FUNCTIONS (ANONYMOUS)
--------------------------------------------------------------------------------
# Basic lambda
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda with multiple parameters
add = lambda a, b: a + b
print(add(10, 20))  # Output: 30

================================================================================

7. MAP FUNCTION
--------------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]

# Using map with lambda
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Using map with defined function
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]

================================================================================

8. FILTER FUNCTION
--------------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]

# Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(greater_than_5)  # Output: [6, 7, 8, 9, 10]

================================================================================

9. REDUCE FUNCTION
--------------------------------------------------------------------------------
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Calculate sum using reduce
total = reduce(lambda a, b: a + b, numbers)
print(total)  # Output: 15

# Calculate product
product = reduce(lambda a, b: a * b, numbers)
print(product)  # Output: 120

# Find maximum
max_num = reduce(lambda a, b: a if a > b else b, numbers)
print(max_num)  # Output: 5

================================================================================

10. ZIP FUNCTION
--------------------------------------------------------------------------------
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Chennai", "Bangalore", "Vellore"]

# Combine multiple lists
combined = list(zip(names, ages, cities))
print(combined)
# Output: [('Alice', 25, 'Chennai'), ('Bob', 30, 'Bangalore'), ('Charlie', 35, 'Vellore')]

# Iterate through zipped data
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old from {city}")

================================================================================

11. ENUMERATE FUNCTION
--------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry", "mango"]

# Get index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry
# 3: mango

# Start from custom index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

================================================================================

12. HIGHER-ORDER FUNCTIONS
--------------------------------------------------------------------------------
# Function that accepts another function as parameter
def apply_operation(func, value):
    return func(value)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

print(apply_operation(square, 5))  # Output: 25
print(apply_operation(cube, 5))    # Output: 125

================================================================================

13. CLOSURES (NESTED FUNCTIONS)
--------------------------------------------------------------------------------
def outer_function(x):
    """Outer function that returns inner function"""
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
add_ten = outer_function(10)

print(add_five(10))  # Output: 15
print(add_ten(10))   # Output: 20

================================================================================

14. DECORATORS
--------------------------------------------------------------------------------
def my_decorator(func):
    """Decorator that adds functionality before and after function call"""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call

================================================================================

15. RECURSIVE FUNCTIONS
--------------------------------------------------------------------------------
def factorial(n):
    """Calculate factorial using recursion"""
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
print(factorial(6))  # Output: 720

# Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55

================================================================================

16. TYPE HINTS (MODERN PYTHON)
--------------------------------------------------------------------------------
def add(a: int, b: int) -> int:
    """Function with type hints"""
    return a + b

def greet(name: str, age: int) -> str:
    return f"{name} is {age} years old"

print(add(5, 10))              # Output: 15
print(greet("Saravanan", 25))  # Output: Saravanan is 25 years old

================================================================================
                              QUICK REFERENCE TABLE
================================================================================

| Function      | Purpose                          | Example                  |
|---------------|----------------------------------|--------------------------|
| def           | Define function                  | def func():              |
| lambda        | Anonymous function               | lambda x: x+1            |
| map()         | Apply function to iterable       | map(func, list)          |
| filter()      | Filter elements                  | filter(condition, list)  |
| reduce()      | Aggregate values                 | reduce(func, list)       |
| zip()         | Combine iterables                | zip(list1, list2)        |
| enumerate()   | Get index + value                | enumerate(list)          |
| *args         | Variable positional args         | def func(*args)          |
| **kwargs      | Variable keyword args            | def func(**kwargs)       |

================================================================================
                              PRACTICE EXERCISE
================================================================================

# Create a function that:
# 1. Takes a list of numbers
# 2. Filters even numbers
# 3. Squares them
# 4. Returns the sum

def process_numbers(numbers):
    evens = filter(lambda x: x % 2 == 0, numbers)
    squared = map(lambda x: x**2, evens)
    return sum(squared)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = process_numbers(nums)
print(result)  # Output: 220 (4+16+36+64+100)

================================================================================
                              END OF DOCUMENT
================================================================================'''