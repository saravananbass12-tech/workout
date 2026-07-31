================================================================================
                    10 ADVANCED PYTHON QUESTIONS & ANSWERS
================================================================================

QUESTION 1: DECORATORS
--------------------------------------------------------------------------------
Q: What does this code print?

def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()

ANSWER:
Before
Hello
After

--------------------------------------------------------------------------------

QUESTION 2: LIST COMPREHENSION WITH CONDITION
--------------------------------------------------------------------------------
Q: What is the output?

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x for x in numbers if x % 2 == 0 if x > 5]
print(result)

ANSWER:
[6, 8, 10]

--------------------------------------------------------------------------------

QUESTION 3: LAMBDA & MAP
--------------------------------------------------------------------------------
Q: What does this print?

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)

ANSWER:
[1, 4, 9, 16]

--------------------------------------------------------------------------------

QUESTION 4: GENERATORS
--------------------------------------------------------------------------------
Q: What is the output?

def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g), next(g), next(g))

ANSWER:
1 2 3

--------------------------------------------------------------------------------

QUESTION 5: EXCEPTION HANDLING
--------------------------------------------------------------------------------
Q: What prints?

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error")
finally:
    print("Done")

ANSWER:
Error
Done

--------------------------------------------------------------------------------

QUESTION 6: CLASS & INHERITANCE
--------------------------------------------------------------------------------
Q: What is the output?

class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

obj = Child()
obj.show()

ANSWER:
Child
(Method overriding - child class method overrides parent method)

--------------------------------------------------------------------------------

QUESTION 7: __INIT__ AND __STR__
--------------------------------------------------------------------------------
Q: What prints?

class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person({self.name})"

p = Person("Alice")
print(p)

ANSWER:
Person(Alice)

--------------------------------------------------------------------------------

QUESTION 8: DICTIONARY COMPREHENSION
--------------------------------------------------------------------------------
Q: What is the output?

nums = [1, 2, 3, 4]
squares = {x: x**2 for x in nums}
print(squares)

ANSWER:
{1: 1, 2: 4, 3: 9, 4: 16}

--------------------------------------------------------------------------------

QUESTION 9: CLOSURES
--------------------------------------------------------------------------------
Q: What does this print?

def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(10))

ANSWER:
15

--------------------------------------------------------------------------------

QUESTION 10: *ARGS AND **KWARGS
--------------------------------------------------------------------------------
Q: What is the output?

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, name="John", age=25)

ANSWER:
(1, 2, 3)
{'name': 'John', 'age': 25}

================================================================================
                              TOPICS COVERED
================================================================================
1. Decorators          - Function wrappers with @syntax
2. List Comprehension  - Multiple conditions in single line
3. Lambda & Map        - Anonymous functions with map()
4. Generators          - yield keyword and next()
5. Exception Handling  - try-except-finally blocks
6. Inheritance         - Method overriding in OOP
7. Special Methods     - __init__ and __str__
8. Dict Comprehension  - Dictionary creation in one line
9. Closures            - Nested functions and scope
10. *args/**kwargs     - Variable length arguments

================================================================================
