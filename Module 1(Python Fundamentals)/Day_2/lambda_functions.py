square = lambda x: x*x
# lambda parameters: expression
print(square(8))

numbers = [1,2,3,4,5]

double = list(map(lambda x:x*2, numbers))
# map() applies a function to every element of an iterable (like a list).
# map(function, iterable)
print(double)

even = list(filter(lambda x:x%2==0, numbers))
# filter() keeps only the elements for which the function returns True.
# filter(function, iterable)
print(even)