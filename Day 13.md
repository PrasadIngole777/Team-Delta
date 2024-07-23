## Lambda Function
```
Map takes a function and an iterable (e.g., list, string) (or more than one iterable), applies the function to all items in that input iterables, and returns map object which is lazy.
```
### Syntax:
```py
lambda arguments: expression
```
### Example:
```py
add_lambda = lambda x, y: x + y
print(add_lambda(3, 4))  # Output: 7
```
## Map Function
```
A lambda function is a nameless function which is defined using the keyword namely as 'lambda'. Typically they
are used for functions that preform a one-off operation and not reused across the code base
```
### Syntax:
```py
map(function, iterable)
```
### Example:
```py
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```
## Filter Function
```
The filter function constructs an iterator from elements of an iterable for which a function returns true.
```
### Syntax:
```py
filter(function, iterable)
```
### Example:
```py
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]
```
## Reduce Function
```
The reduce function, which you can find in the functools module, has an impact on an iterable.
It uses a rolling calculation on pairs of values that follow each other turning the whole thing into one value.
```
### Syntax:
```py
from functools import reduce
reduce(function, iterable)
```
### Example:
```py
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
```
