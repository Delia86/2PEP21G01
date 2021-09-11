#example of nested functions
from time import sleep
from functools import wraps


def conversation():
    def hello():
        print("Hello")

    return hello
# hello() -  function exists only inside parent function namespace we cannot call it outside "conversation"

# Decorator
def delay(seconds=0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """This function has some other docstring"""
            print('print before')
            result = func(*args, **kwargs)
            print(f"Sleeping for {seconds} seconds")
            sleep(seconds)
            print('print after')
            return result
        return wrapper
    return decorator


@delay(3)
def func1(value):
    """This function has some docstring"""
    print(f'This does nothing but prints: {value}')
    sleep(1)
    return "My func1 return"

# func1 = decorator(func1,)

if __name__ == "__main__":
    hello = conversation()
    print(type(hello))
    hello()

    result =delay(func1)
    print(type(result))
    result()

    # Some user does:
func1(6)