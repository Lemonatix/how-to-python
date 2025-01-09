def before_after_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
    return wrapper

@before_after_decorator 
def say_hello(name):
    print(f"Hello {name}")

say_hello("John")