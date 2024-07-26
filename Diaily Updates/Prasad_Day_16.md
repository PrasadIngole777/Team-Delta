Numpy Array :
        
    --> Numpy arrays are used for mathematical and statistical computations.
    
    --> Can manipulate and understand multi-dimensional data.
    

  Creating a numpy array :

    import numpy as np
    
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    
    print(arr)

Array Indexing : Extracting and Modifying Elements in Arrays

Example : 

    import numpy as np

    arr = np.array([[1, 2, 3], [4, 5, 6]])
    
    print("1st Row: ", arr[0])
    
    print("2nd Column: ", arr[:, 1])

Converting lists to multi-dimensional Numpy arrays

    import numpy as np

    list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    arr = np.array(list_data)
    
    print(arr)

Array Slicing : Selecting Specific Parts of Arrays is called array slicing.

Example : 

    import numpy as np

    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    print("First Two Rows: ", arr[:2])
    
    print("Second Column: ", arr[:, 1:2])

Array Broadcasting : Dealing with Conditions for Entire Array is called array boardcasting.

Example : 

    import numpy as np

    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    arr[arr > 5] = 10
    
    print(arr)

Iterating Numpy arrays through Loop :

    import numpy as np

    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    for i in range(len(arr)):
    
        for j in range(len(arr[i])):
        
            arr[i, j] *= 2
            
    print(arr)













    












    
