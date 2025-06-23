def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
@my_decorator
def say_hello():
    print("hello")
say_hello()
#List
list_=[1,2,[3,4,["python"]]]
print(list_[2][2][0])
#Sorting
lst=[
    {"name" : "umair","money":50 },
    {"name" : "umairr","money":23 },
    {"name" : "ali","money":45 },
    {"name" : "umairrr","money":43 }
]
sortedd=sorted(lst,key=lambda lst:lst["money"],reverse=True)
print(sortedd)
#Decorator
def decorator_function(func):
    def wrapper_function():
        print("before")
        func()
        print("after")
    return wrapper_function
@decorator_function
def say_hello():
    print("Hello")
say_hello()
#Greeter
def myy_decorator(rep_count):
    def my_decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(rep_count):
                print(f"calling {func.__name__} with argument {args}")
                result=func(*args,**kwargs)
                print(f"{func.__name__} returned {result}")
            return result
        return wrapper
    return my_decorator
@myy_decorator(3)
def greet(name):
    print("hello",name)
    return f"Greeted {name}"
greet("ali")
#Sleeper
import time
def timing_decorator(func):
    def wrapper():
        start_time=time.time()
        func()
        end_time=time.time()
        print(f"execution time: {end_time-start_time}sec")
    return wrapper
@timing_decorator
def sleep_():
    time.sleep(2)
    print("done")
sleep_()
#Authenticator
def require_authentication(func):
    def wrapper(user):
        if not user.get('is_authenticated'):
            print("user is not authenticated")
            return None
        return func(user)
    return wrapper
@require_authentication
def get_dashboard(user):
    return f"Welcome to the dashboard, {user['username']}"
user1={'username': 'ali', 'is_authenticated': True}
user2={'username': "umer", 'is_authenticated': False}
print(get_dashboard(user1))
print(get_dashboard(user2))
#Adder
def log_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        result=func(*args,**kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
@log_decorator
def add(a,b):
    return a,b
@log_decorator
def greetings(name,greeting="hi"):
    return f"{name}, {greeting}"
add(2,3)
greetings("ali",greeting="hello")
#Greeting Count
def main_decorator(rep_count):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(rep_count):
                print(f"calling {func.__name__} with arguments")
                main_perf=func(*args,**kwargs)
                print(f"{func.__name__} gives {main_perf}")
            return main_perf
        return wrapper
    return decorator
@main_decorator(1)
def greetings(name):
    print("hello",name)
    return name
greetings("ali")
#Wrapper Addition
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("calling before")
        result=func(*args,**kwargs)
        print(f"returning {result}")
        return result
    return wrapper
@my_decorator
def add(a,b):
    return a+b
print(add(3,4))
#Bold
def bold_decorator(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper
def italic_decorator(func):
    def wrapper():
        return f"<i>{func()}<i/>"
    return wrapper
@bold_decorator
@italic_decorator
def text():
    return "hello"
print(text())
#Using Functools
import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Executing decorated function")
        return func(*args, **kwargs)
    return wrapper
@my_decorator
def greet(name):
    """Greet a person."""
    print(f"Hello, {name}!")
print(greet.__name__) 
print(greet.__doc__)   
greet("ali")
#Rand and Time
import random
import time
def main_decorator(coun):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(coun):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    print(f"attempt {_+1} failed as {e}")
                    time.sleep(1)
            print(f"failed after {coun} tries")
        return wrapper
    return decorator
@main_decorator(3)
def to_repeat():
    if random.choice([True,False]):
        raise ValueError("failure")
    return "success"
print(to_repeat())

