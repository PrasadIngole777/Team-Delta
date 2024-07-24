Generator functions : 

    Generator functions are a type of function that return a generator object, which can be iterated over like a 
    list or tuple. Generators are more memory-efficient than lists because they generate values on-the-fly instead 
    of storing them all in memory at once.

Example :
    
      def count_up_to(n):
        for i in range(n):
          yield i

      for i in count_up_to(10):
        print(i)

Iterators : 
    
    Iterators are objects that can be iterated upon, providing a sequence of data one element at a time.
    
Advantages :

    Memory efficiency: Iterators generate and return each element on-the-fly, rather than storing all elements in
                       memory.
    Flexibility:       They can be used to iterate over custom data structures or manipulated data.
    Code organization: Custom iterators can help simplify and organize code by encapsulating complex iteration 
                       logic.
