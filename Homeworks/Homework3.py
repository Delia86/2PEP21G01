"""
Counted List
Create a class for an list like object based on UserList wrapper
https://docs.python.org/3/library/collections.html#collections.UserList
That object should have a method to return a Counter
https://docs.python.org/3/library/collections.html#collections.Counter
for all objects in the list
Counter should be updated automatically for at lest 2 methods (append, pop)
"""

from collections import UserList,Counter



class Example(UserList):

    def get_counter(self):
        my_counter = Counter(my_list)
        return my_counter


    def append(self, item):
            global y
            super(Example,self).append(item)
            y=self.get_counter()

    def pop(self,i) :
            global y
            super(Example, self).pop(i)
            y = self.get_counter()









my_list=Example(['1','2,','3'])
y=my_list.get_counter()
print(y)
my_list.append('3')
print(y)
my_list.pop(1)
print (y)





