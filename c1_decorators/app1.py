# Some user does:
# from modul1 import func1
# print(80*"#")
# print(func1("Delia"))
#
# print(80*"#")
# print(func1.__name__)
# print(func1.__doc__)

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function #equals with display=decorator_function(display)
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print ('display_info ran with args({},{})'.format(name,age))

display_info('Delia',35)

display()