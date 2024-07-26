Numpy Multi Dimensional Arrays :

    --> A multi-dimensional array is an array of arrays.
    
    --> In memory, multi-dimensional arrays are stored as a single block of memory, with each element
    
        being stored in a contiguous block.
    
    --> The shape of a multi-dimensional array refers to the number of dimensions and the size of each 
    
        dimension.

Representation and Access of Elements in Arrays : 

    --> In a two-dimensional array, elements are stored in rows and columns, with each element being addressed 
    
        by its row and column index.
    
    --> In general, elements in an n-dimensional array are addressed using n indices.

    --> To access an element in a multi-dimensional array, the program first computes the memory address of the 
    
        element using the indices and the knowledge of the array's shape and byte-offset.

    --> The program then retrieves or modifies the value stored at that memory location.


All Numpy Oprations On 2D Array :

    import numpy as np

    # Create a 2D array (matrix) using a list of lists
    
    array_2d = np.array([[1, 2, 3], [4, 5, 6]])  
    print(array_2d)

    # Accessing individual elements
    
    element = array_2d[1, 2]  # Element in the second row, third column
    print("\nElement at (1, 2):", element)

    # Accessing entire rows and columns
    
    first_row = array_2d[0, :]
    print("\nFirst Row:", first_row)

    second_column = array_2d[:, 1]
    print("Second Column:", second_column)

    # Matrix multiplication (dot product)
    
    matrix_b = np.array([[7, 8], [9, 10], [11, 12]])
    dot_product = np.dot(array_2d, matrix_b)
    print(dot_product)

    # Transpose of a matrix
    
    transpose = array_2d.T
    print(transpose)

    # Inverse of a matrix
    
    square_matrix = np.array([[1, 2], [3, 4]])
    inverse = np.linalg.inv(square_matrix)
    print(inverse)

    # Determinant of a matrix
    
    determinant = np.linalg.det(square_matrix)
    print(determinant)




















    
