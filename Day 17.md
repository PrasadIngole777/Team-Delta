### Advanced multidimensional array operations.
Definition:
```
A multidimensional array is defined as a collection of elements, each of which is identified by a tuple of indices (i, j, k, ...),where each index corresponds to a dimension.
The number of dimensions is called the rank or order of the array.
```
## Finding the dimensions of the Array:
```py
>>> import numpy as np  
>>> arr = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 23]])  
  
>>> print(arr.ndim)  #o/p: 2
```
## Finding the shape and size of the array
```py
import numpy as np  
a = np.array([[1,2,3,4,5,6,7]])  
print("Array Size:",a.size)  
print("Shape:",a.shape)  #output:Array Size: 7
                                 Shape: (1, 7)
```
## Reshaping the array objects
```py
import numpy as np  
a = np.array([[1,2],[3,4],[5,6]])  
print("printing the original array..")  
print(a)  
a=a.reshape(2,3)  
print("printing the reshaped array..")  
print(a)  
```
Output:
```
printing the original array..
[[1 2]
 [3 4]
 [5 6]]
printing the reshaped array..
[[1 2 3]
 [4 5 6]]
```
## Slicing in the Array
```py
import numpy as np  
a = np.array([[1,2],[3,4],[5,6]])  
print(a[0,1])  
print(a[2,0])  #output:2
                       5
```
## Finding the maximum, minimum, and sum of the array elements
```py
import numpy as np  
a = np.array([1,2,3,10,15,4])  
print("The array:",a)  
print("The maximum element:",a.max())  
print("The minimum element:",a.min())  
print("The sum of the elements:",a.sum())  
```
Output:
```
The array: [ 1  2  3 10 15  4]
The maximum element: 15
The minimum element: 1
The sum of the elements: 35
```
## Array Concatenation
```py
import numpy as np  
a = np.array([[1,2,30],[10,15,4]])  
b = np.array([[1,2,3],[12, 19, 29]])  
print("Arrays vertically concatenated\n",np.vstack((a,b)));  
print("Arrays horizontally concatenated\n",np.hstack((a,b)))
```
Output:
```
Arrays vertically concatenated
 [[ 1  2 30]
 [10 15  4]
 [ 1  2  3]
 [12 19 29]]
Arrays horizontally concatenated
 [[ 1  2 30  1  2  3]
 [10 15  4 12 19 29]]
```
