**Day 9: Efficient Data Manipulation Techniques**
**1. List Comprehensions**

Definition: A concise way to create lists. They can include conditions and multiple loops for filtering and transformation.
Syntax: [expression for item in iterable if condition]
Example:
 
even_numbers = [x for x in range(10) if x % 2 == 0]


**2. Generator Expressions**

Definition: Similar to list comprehensions but generate items one by one. They are memory efficient, especially with large datasets.
Syntax: (expression for item in iterable if condition)
Example:
 
squares_gen = (x**2 for x in range(10))


**3. Other Techniques**

Zip Function: Combines multiple iterables into a single iterator of tuples.
python
Copy code
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
student_scores = zip(names, scores)
Map Function: Applies a function to all items in an input list.
 
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
Filter Function: Filters items in an iterable based on a function.
 
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
