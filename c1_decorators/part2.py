#built in decorators

class MyClass:
    my_var=None

    def __init__(self,my_var):
        self.my_var=my_var


        @classmethod #provides class of object instead of object as first arg
        def check_classmethod(cls):
            print(f'Value is" {cls.my_var}')

        @staticmethod #removes the first arg from method transforming it into a function
        def check_staticmethod():
            # print(self.my_var)
            print ('This method does not have any object info')

        @property #this will create a property called my_string_var that does not need to be called to return a value
        def my_string_var(self):
            return self.my_var

        @my_string_var.setter # this allow us to set "my_string_var" as a variable
        def my_string_var

