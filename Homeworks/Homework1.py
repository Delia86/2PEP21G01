""" Create 2 decorators that will get applied to the function below
    1) first decorator applied insures that input arguments and output values are converted to the arguments provided as decorator
    2) second decorator will write each output values on a new line in a file that matches the function name
    Use functions created by you
"""

from functools import wraps

def greet_person(counts:int):
    def decorator_greet(func):
        @ wraps(func)
        def wrapper(*args,**kwargs):
            for count in range(counts):
                result= func(*args,**kwargs)
            print(f'{func.__name__} run with :{counts} counts')

            return result

        return wrapper

    return decorator_greet

def my_log(func):
    @wraps (func)
    def wrapper(*args,**kwargs):
        with open('log.txt','w') as file:
            for arg in args:
                file.write(f'{func.__name__} greeted {arg}'+'\n')
        result=func(*args,**kwargs)
        return result
    return wrapper



@greet_person(3)
@my_log
def say_hello(name):
    print(f'Hello:{name},how are you?')

say_hello('Anna')

