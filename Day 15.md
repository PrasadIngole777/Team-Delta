# Numpy
An amazing library for numerical computing in Python is NumPy (Numerical Python). It deals with the manipulation of arrays, matrices and other mathematical operations that can be applied to these data structures.

### Key Features of NumPy:

-Fast and space-efficient array: N-dimensional array object(ndarray).

-Broadcasting: Performing arithmetic operations on arrays having different shapes.

-Vectorization: Replacing explicit loops with array expressions.

-Linear algebra, random number generation, etc.
## To use NumPy, you need to import it:
```py
import numpy as np
```
## Creating array 
```py
arr = np.array([1, 2, 3, 4, 5])
print(arr)
```
## Array attributes:
```py
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)     # Output: (2, 3)
print(arr.ndim)      # Output: 2 (number of dimensions)
print(arr.size)      # Output: 6 (total number of elements)
print(arr.dtype)     # Output: int64 (data type of elements)
```
