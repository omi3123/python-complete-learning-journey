#1
list_=[1,2,3,4,5]
iter_items=iter(list_)
print(next(iter_items))
#Iterator
class Iterator:
    def __init__(self,maximum_value):
        self.maximum_value=maximum_value
        self.current_value=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_value<self.maximum_value:
            self.current_value+=1
            return self.current_value
        else:
            raise StopIteration
iter_items=Iterator(3)
for value in iter_items:
    print(value)
#Generator
def my_generator():
    yield 1
    yield 2
    yield 3
generator=my_generator()
print(next(generator))
print(next(generator))
#Counter
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        current=self.current
        self.current+=1
        return current
def generator_counter(low, high):
    current = low
    while current <= high:
        yield current
        current += 1
counter_iter = Counter(1, 3)
for num in counter_iter:
    print(num)
for num in generator_counter(1, 3):
    print(num)
#FibIteraator
class FibonacciIterator:
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        fib_number = self.b
        self.a, self.b = self.b, self.a + self.b
        return fib_number
# Using the Fibonacci iterator
fib_iterator = FibonacciIterator()
for _ in range(10):
    print(next(fib_iterator))
#FibGenerator
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b
fib_gen = fibonacci_generator()
for _ in range(1,10):
    print(next(fib_gen))