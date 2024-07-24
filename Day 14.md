## Iterators
An iterator is an object that allows you to iterate over a sequence (such as a list, tuple, or string) and access its elements one at a time.
### Example:
```py
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

print(next(my_iter))  # prints 1
print(next(my_iter))  # prints 2
print(next(my_iter))  # prints 3
print(next(my_iter))  # prints 4
print(next(my_iter))  # prints 5
```
## Generators
A generator is a special type of iterator that can be used to generate a sequence of values on the fly, rather than storing them all in memory at once.
### Example:
```py
def my_gen():
    for i in range(5):
        yield i

my_gen_iter = my_gen()

print(next(my_gen_iter))  # prints 0
print(next(my_gen_iter))  # prints 1
print(next(my_gen_iter))  # prints 2
print(next(my_gen_iter))  # prints 3
print(next(my_gen_iter))  # prints 4
```
