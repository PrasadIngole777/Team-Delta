
#### Day 16: Indexing, Slicing, and Reshaping Arrays

**1. Indexing and Slicing**

- **Indexing**: 
  - Access elements in a Numpy array using indices.
  - Example:
    ```python
    arr = np.array([1, 2, 3, 4, 5])
    print(arr[0])  # Output: 1
    print(arr[-1])  # Output: 5
    ```

- **Slicing**: 
  - Access subarrays using slices.
  - Syntax: `array[start:stop:step]`
  - Example:
    ```python
    arr = np.array([1, 2, 3, 4, 5])
    subarr = arr[1:4]  # Output: array([2, 3, 4])
    ```

- **Multidimensional Indexing and Slicing**:
  - Example:
    ```python
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    element = matrix[1, 2]  # Output: 6
    row = matrix[1, :]  # Output: array([4, 5, 6])
    col = matrix[:, 1]  # Output: array([2, 5, 8])
    ```

**2. Reshaping Arrays**

- **Reshape**: 
  - Change the shape of an array without changing its data.
  - Example:
    ```python
    arr = np.arange(6)
    reshaped = arr.reshape((2, 3))  # Output: array([[0, 1, 2], [3, 4, 5]])
    ```

- **Flatten**: 
  - Convert a multidimensional array into a one-dimensional array.
  - Example:
    ```python
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    flat = matrix.flatten()  # Output: array([1, 2, 3, 4, 5, 6])
    ```

- **Transpose**: 
  - Swap the axes of an array.
  - Example:
    ```python
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    transposed = matrix.T  # Output: array([[1, 4], [2, 5], [3, 6]])
    ```
 
