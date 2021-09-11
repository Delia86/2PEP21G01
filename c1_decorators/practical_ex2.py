# import datetime
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         with open('logs.txt','a') as file:
#             file.write('Called function with'+''.join([str(arg)for arg in args ])+'at'+str(datetime.datetime.now())+'\n')
#             val=func(*args, **kwargs)
#             return val
#     return wrapper
#
# @log
# def run(a,b,c=9):
#     print(a+b+c)
# run(1,3,c=9)
# run(2,6,c=6)


from functools import wraps

def adding_numbers(num1,num2):
    def decorator_add(func):
        @ wraps(func)
        def wrapper(*args,**kwargs):
            print(f'{func.__name__} adds {num1},{num2}')
            result=func(*args,**kwargs)

            return result

        return wrapper

    return decorator_add

def my_log(func):
    @wraps (func)
    def wrapper(*args,**kwargs):
        with open('log.txt','w') as file:
            for arg in args:
                file.write(f'{func.__name__} greeted {arg}'+'\n')
        result=func(*args,**kwargs)
        return result
    return wrapper



@adding_numbers(3,5)
@my_log
def add_num(numbers:str):
    print(f'{numbers} are {adding_numbers}')

add_num(3)

