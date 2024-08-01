 
#### Day 13-14: Functional Programming in Python

Functional programming is a programming paradigm where functions are first-class citizens,
meaning they can be passed as arguments, returned from other functions, and assigned to variables. 
It emphasizes immutability, pure functions, and higher-order functions.
Python supports functional programming concepts alongside its other paradigms, offering versatile ways to write clean and efficient code.

#### Day 13: Lambda Functions, Map, Filter, and Reduce

**1. Lambda Functions**

- **Definition**: Anonymous, inline functions defined with the `lambda` keyword. They can have any number of arguments but only one expression. The result of the expression is automatically returned.
- **Syntax**: 
  ```python
  lambda arguments: expression
  ```
- **Example**:
  ```python
  add = lambda x, y: x + y
  print(add(2, 3))  # Output: 5
  ```

- **Use Cases**: Often used for short, throwaway functions, especially as arguments to higher-order functions like `map`, `filter`, and `sorted`.

**2. Map Function**

- **Definition**: Applies a given function to all items in an input iterable (e.g., list, tuple) and returns a map object (which can be converted to a list, tuple, etc.).
- **Syntax**: 
  ```python
  map(function, iterable)
  ```
- **Example**:
  ```python
  numbers = [1, 2, 3, 4]
  squared = list(map(lambda x: x**2, numbers))
  print(squared)  # Output: [1, 4, 9, 16]
  ```

**3. Filter Function**

- **Definition**: Filters elements from an iterable, returning only those for which the given function returns `True`.
- **Syntax**: 
  ```python
  filter(function, iterable)
  ```
- **Example**:
  ```python
  numbers = [1, 2, 3, 4, 5, 6]
  even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
  print(even_numbers)  # Output: [2, 4, 6]
  ```

**4. Reduce Function**

- **Definition**: Applies a binary function cumulatively to the items of an iterable, reducing the iterable to a single value. It is part of the `functools` module.
- **Syntax**: 
  ```python
  functools.reduce(function, iterable[, initializer])
  ```
- **Example**:
  ```python
  from functools import reduce
  numbers = [1, 2, 3, 4]
  product = reduce(lambda x, y: x * y, numbers)
  print(product)  # Output: 24
  ```
 
