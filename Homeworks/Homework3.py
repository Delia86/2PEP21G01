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
        self.my_counter= Counter(my_list)
        return self.my_counter


    def append(self, item):
            super(Example,self).append(item)
            self.my_counter[item]+=1

    def pop(self,i) :
            super(Example, self).pop(i)
            self.my_counter[i]-= 1









my_list=Example(['1','2,','3'])
y=my_list.get_counter()
print(y)
my_list.append('3')
print(y)
my_list.pop(1)
print (y)





