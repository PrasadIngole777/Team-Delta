
#### Day 14: Iterators, Generators, and Advanced Functional Programming Modules

**1. Iterators**

- **Definition**: Objects that can be iterated upon. They implement two methods: `__iter__()` and `__next__()`.
- **Creating Iterators**: 
  - Use the `iter()` function to get an iterator object.
  - Use the `next()` function to get the next value from the iterator.
- **Example**:
  ```python
  my_list = [1, 2, 3]
  iterator = iter(my_list)
  print(next(iterator))  # Output: 1
  print(next(iterator))  # Output: 2
  print(next(iterator))  # Output: 3
  ```

**2. Generators**

- **Definition**: Special iterators defined using a function with the `yield` statement. Generators generate values on the fly and are more memory efficient than traditional lists.
- **Syntax**:
  ```python
  def generator_function():
      yield value
  ```
- **Example**:
  ```python
  def count_up_to(max):
      count = 1
      while count <= max:
          yield count
          count += 1

  counter = count_up_to(5)
  print(next(counter))  # Output: 1
  print(next(counter))  # Output: 2
  print(list(counter))  # Output: [3, 4, 5]
  ```

- **Use Cases**: Generators are useful when dealing with large datasets or streams of data, as they do not require storing all the values in memory.

**3. `functools` Module**

- **Overview**: The `functools` module provides higher-order functions and operations on callable objects.
- **Key Functions**:
  - `reduce()`: Reduces a sequence of elements to a single value.
  - `partial()`: Fixes a certain number of arguments of a function and generates a new function.
  - `lru_cache()`: Decorator for caching function results.
- **Example**:
  ```python
  from functools import lru_cache

  @lru_cache(maxsize=None)
  def fibonacci(n):
      if n <= 1:
          return n
      return fibonacci(n-1) + fibonacci(n-2)

  print(fibonacci(10))  # Output: 55
  ```

**4. `itertools` Module**

- **Overview**: The `itertools` module provides a collection of tools for handling iterators. It includes functions for creating iterators for efficient looping.
- **Key Functions**:
  - `count()`: Infinite counting iterator.
  - `cycle()`: Infinite iterator cycling through an iterable.
  - `repeat()`: Repeats an object a specified number of times.
  - `chain()`: Chains multiple iterables together.
  - `islice()`: Slices an iterator.
  - `combinations()`: Returns all possible combinations of elements.
  - `permutations()`: Returns all possible permutations of elements.
- **Example**:
  ```python
  from itertools import count, cycle, islice

  # Infinite counting iterator
  counter = count(start=1, step=2)
  print(next(counter))  # Output: 1
  print(next(counter))  # Output: 3

  # Cycling through a list
  cycle_list = cycle(['A', 'B', 'C'])
  print(next(cycle_list))  # Output: A
  print(next(cycle_list))  # Output: B

  # Slicing an iterator
  iterator = count()
  sliced = islice(iterator, 10)
  print(list(sliced))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

 
