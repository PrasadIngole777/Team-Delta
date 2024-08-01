### Advanced Python Programming Concepts: Week 3 - Numpy and Matplotlib

#### Day 15-17: Mastering Numpy

Numpy is a fundamental package for scientific computing in Python. 
It provides support for arrays, matrices, and many mathematical functions. 
Understanding Numpy is crucial for data analysis, machine learning, and other scientific applications.
The following breakdown provides detailed coverage of key concepts and techniques in Numpy.

#### Day 15: Introduction to Numpy and Basic Array Operations

**1. Introduction to Numpy**

- **What is Numpy?**: Numpy is a library for numerical computations in Python. It provides efficient array operations and is widely used in data analysis, machine learning, and scientific computing.
- **Key Features**: 
  - N-dimensional array object (ndarray).
  - Mathematical functions for fast operations on arrays.
  - Tools for integrating C/C++ and Fortran code.
  - Linear algebra, Fourier transform, and random number capabilities.

- **Installation**:
  ```sh
  pip install numpy
  ```

**2. Creating Numpy Arrays**

- **Array Creation**:
  - **From Lists**:
    ```python
    import numpy as np
    array = np.array([1, 2, 3])
    ```
  - **Using Functions**:
    - `np.zeros()`: Creates an array of zeros.
    - `np.ones()`: Creates an array of ones.
    - `np.arange()`: Creates an array with a range of values.
    - `np.linspace()`: Creates an array with evenly spaced values.
    - `np.random.random()`: Creates an array with random values.
  - **Example**:
    ```python
    zeros = np.zeros((3, 3))
    ones = np.ones((2, 4))
    range_array = np.arange(0, 10, 2)
    linspace_array = np.linspace(0, 1, 5)
    random_array = np.random.random((2, 3))
    ```

**3. Basic Array Operations**

- **Arithmetic Operations**: 
  - Element-wise addition, subtraction, multiplication, and division.
  - Example:
    ```python
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = a + b  # Output: array([5, 7, 9])
    d = a * b  # Output: array([ 4, 10, 18])
    ```
- **Universal Functions (ufuncs)**: 
  - Numpy provides mathematical functions such as `np.sqrt()`, `np.exp()`, `np.sin()`, etc.
  - Example:
    ```python
    arr = np.array([1, 4, 9, 16])
    sqrt_arr = np.sqrt(arr)  # Output: array([1., 2., 3., 4.])
    ```

- **Aggregations**:
  - Functions like `np.sum()`, `np.mean()`, `np.std()`, `np.min()`, and `np.max()` can be applied to arrays.
  - Example:
    ```python
    arr = np.array([1, 2, 3, 4])
    total = np.sum(arr)      # Output: 10
    mean_value = np.mean(arr)  # Output: 2.5
    ```
 
