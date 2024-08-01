**Day 10: Implementation of Decorators and Context Managers**


**1. Python Decorators**
Definition: Functions that modify the behavior of other functions or methods. They take a function as an argument and return a new function.
Syntax:
python
Copy code
@decorator_function
def my_function():
    pass

Equivalent to:

def my_function():
    pass
my_function = decorator_function(my_function)

**Use Cases:** Logging, memoization, access control, and more.

Example:

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def add(a, b):
    return a + b


**2. Context Managers**

Definition: Used to properly manage resources, ensuring they are acquired and released appropriately. Implemented using the __enter__ and __exit__ methods.

Syntax:

with context_manager() as var:
    pass
    
    
Equivalent to:

var = context_manager.__enter__()
try:
    pass
finally:
    context_manager.__exit__()
    
Example:

class FileManager:
    def __enter__(self):
        self.file = open('example.txt', 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager() as file:
    content = file.read()
print(content)
