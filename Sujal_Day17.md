
#### Day 17: Broadcasting, Vectorization, and Advanced Multidimensional Array Operations

**1. Broadcasting**

- **Definition**: A method used by Numpy to perform arithmetic operations on arrays of different shapes. It automatically expands the dimensions of the smaller array to match the larger array.
- **Rules**:
  - If the arrays do not have the same rank, prepend the shape of the smaller array with 1s.
  - The size in each dimension of the output shape is the maximum of the input sizes.
  - An array with a size of 1 in a particular dimension can be stretched to match the other array's size in that dimension.

- **Example**:
  ```python
  a = np.array([1, 2, 3])
  b = np.array([[10], [20], [30]])
  result = a + b
  # Output: array([[11, 12, 13],
  #                [21, 22, 23],
  #                [31, 32, 33]])
  ```

**2. Vectorization**

- **Definition**: The process of converting operations that would normally be performed on scalars or lists into operations on vectors (arrays). This approach leverages Numpy's optimized C backend, leading to significant performance gains.
- **Example**:
  ```python
  # Without vectorization
  result = [x * 2 for x in range(1, 6)]  # Output: [2, 4, 6, 8, 10]

  # With vectorization
  result = np.arange(1, 6) * 2  # Output: array([ 2,  4,  6,  8, 10])
  ```

**3. Advanced Multidimensional Array Operations**

- **Stacking and Splitting Arrays**:
  - **Stacking**:
    - `np.vstack()`: Stack arrays vertically (row-wise).
    - `np.hstack()`: Stack arrays horizontally (column-wise).
    - Example:
      ```python
      a = np.array([1, 2])
      b = np.array([3, 4])
      vertical_stack = np.vstack((a, b))  # Output: array([[1, 2], [3, 4]])
      horizontal_stack = np.hstack((a, b))  # Output: array([1, 2, 3, 4])
      ```

  - **Splitting**:
    - `np.split()`: Split an array into multiple subarrays.
    - Example:
      ```python
      arr = np.array([1, 2, 3, 4, 5, 6])
      split_arr = np.split(arr, 3)  # Output: [array([1, 2]), array([3, 4]), array([5, 6])]
      ```

- **Advanced Indexing Techniques**:
  - **Boolean Indexing**: Use boolean arrays to select elements from an array.
  - **Example**:
    ```python
    arr = np.array([1, 2, 3, 4, 5])
    bool_arr = arr > 2
    result = arr[bool_arr]  # Output: array([3, 4, 5])
    ```

- **Matrix Operations**:
  - Matrix multiplication (`np.dot()`, `@` operator).
  - Example:
    ```python
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    product = np.dot(A, B)  # Output: array([[19, 22], [43, 50

]])
    ```

 
