from collections import OrderedDict

dict_1={1:'1',2:'2',3:'3'}
dict_1[0]='0'
print(dict_1)

dict_2=OrderedDict({1:'1',2:'2',3:'3'})
dict_2[0]='0'
print(dict_2)
print(dict_2.popitem(last=True))
dict_2.move_to_end(2)
print(dict_2)