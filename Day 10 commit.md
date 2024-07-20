# Python Decorators

# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.



# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:



# @decorator_function

# def my_function():

#     pass



# The @decorator_function notation is just a shorthand for the following code:



# def my_function():

#     pass

# my_function = decorator_function(my_function)



# Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.



# Practical use case

# One common use of decorators is to add logging to a function. For example, you could use a decorator to log the arguments and return value of a function each time it is called:



import logging

def log_function_call(func):

    def decorated(*args, **kwargs):

        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        logging.info(f"{func.__name__} returned {result}")

        return result

    return decorated

@log_function_call

def my_function(a, b):

    return a + b

# In this example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function call before and after the original function is called.



# A context manager is a class that defines the __enter__ and __exit__ methods. These methods are used to manage resources, such as files, connections, or locks, in a way that ensures they are properly cleaned up after use.



# The __enter__ method is called when the context manager is entered, and it returns an object that can be used within the context. The __exit__ method is called when the context manager is exited, and it is responsible for releasing any resources acquired during the __enter__ method.



# class FileManager:

#     def __enter__(self):

#         self.file = open('example.txt', 'r')

#         return self.file



#     def __exit__(self, exc_type, exc_val, exc_tb):

#         self.file.close()



# with FileManager() as file:

#     content = file.read()

# print(content)
