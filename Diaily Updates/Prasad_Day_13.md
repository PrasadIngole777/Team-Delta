Lambda Functions : 

    --> Lambda functions are anonymous functions in Python, meaning they are not bound to a name at the time of 
        their creation.
    --> They are often used in situations where a regular function would not be significant.

Syntax :    
      
      lambda arguments: expression

Example : 

      add = lambda x, y: x + y
      result = add(5, 3)
      print(result)

Map, Filter, and Reduce: Applications of Lambda Function

1) Map :

        The map() function applies a given function to each item in an iterable (such as a list) and returns a new
        iterable with the results.
2) Filter

        The filter() function takes in a function and an iterable as input, and returns a new iterable with only the
        elements for which the function returns True.
3) Reduce

        The reduce() function reduces an iterable to a single value by repeatedly applying a given function to its
        elements. It is part of the functools module and must be imported before use.
