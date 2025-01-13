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

# ---------------------
def my_decorator(func):
    def wrapper():
        print("Es passiert etwas vor dem Funktionsaufruf.")
        func()
        print("Es passiert etwas danach.")
    return wrapper

@my_decorator
def sag_hallo():
    print("Servus!")

sag_hallo()