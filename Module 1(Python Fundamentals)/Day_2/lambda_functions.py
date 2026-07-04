square = lambda x: x*x

print(square(8))

numbers = [1,2,3,4,5]

double = list(map(lambda x:x*2, numbers))

print(double)

even = list(filter(lambda x:x%2==0, numbers))

print(even)