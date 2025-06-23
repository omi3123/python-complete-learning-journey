#Args and Kwargs
def something_crazy(*args,**kwargs):
    for arguments in args:
        print(arguments)
    for key,value in kwargs.items():
        print(f"{key} : {value}")
something_crazy(1,2,name="ali",age=21)
#Sum of all
def sum_all(*args):
    total=0
    for num in args:
        total+=num
    return total
print(sum_all(10,20,30,40))
#Profile Build
def build_profile(**kwargs):
    profile={}
    for key,value in kwargs.items():
        profile[key]=value
    return profile
user_profile=build_profile(Name="Ali",Department="SE",Age=21)
print(user_profile)
#Fibonacci Iterator
class FibonacciIterator:
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        fib_number = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib_number
fib_iterator = FibonacciIterator()
for _ in range(10):
    print(next(fib_iterator))

