## Array Indexing
-Array indexing is the same as accessing an array element.
-You can access an array element by referring to its index number.
-The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.
### Example:
```py
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
```
#### Access 2D Arrays
To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.
### Example:
```py
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])
```
## Array Slicing
-Slicing in python means taking elements from one given index to another given index.

-We pass slice instead of index like this: [start:end].

-We can also define the step, like this: [start:end:step].

-If we don't pass start its considered 0

-If we don't pass end its considered length of array in that dimension

-If we don't pass step its considered 1

-Start index:inclusive, End index:exclusive
### Example:
```py
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])  #output:[2 3 4 5]
```
#### Negative Slicing
Use the minus operator to refer to an index from the end.
### Example:
```py
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])  #output:[5 6]
```
STEP
Use the step value to determine the step of the slicing:
### Example:
Return every other element from index 1 to index 5:
```py
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])  #output:[2 4]
```
## Array Reshaping
Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.
### Example:
1D to 3D
```py
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)   #o/p: [[ 1  2  3]
                       [ 4  5  6]
                       [ 7  8  9]
                       [10 11 12]]
```
## Numpy Broadcasting
Broadcasting is a powerful feature in NumPy that allows arrays of different shapes to be used together in arithmetic operations. It works by automatically expanding the smaller array's 
dimensions to match the larger array's dimensions without making copies of the data.
### Example:
```py
import numpy as np  
a = np.array([1,2,3,4,5,6,7])  
b = np.array([2,4,6,8,10,12,14])  
c = a*b;  
print(c)  o/p:[ 2  8 18 32 50 72 98]
```
#### Broadcasting Rules
1. The smaller dimension array can be appended with '1' in its shape.
2. Size of each output dimension is the maximum of the input sizes in the dimension.
3. An input can be used in the calculation if its size in a particular dimension matches the output size or its value is exactly 1.
4. If the input size is 1, then the first data entry is used for the calculation along the dimension.
![numpy-broadcasting](https://github.com/user-attachments/assets/b9e9e795-e342-4fab-a3c5-b12ea4077892)
