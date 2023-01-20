#!/usr/bin/env python
# coding: utf-8
1.What does an empty dictionary's code look like?
sol:
An empty dictionary is often represented by two empty curly brackets
d = {} or d = dict()2.what is the value of dictionary value with key 'foo' and the value 42 ?
sol:
{"foo":42}3.What is the most significant distinction between a dictionary and a list?
sol:
 Dictionaries are represented by {} where as listed are represented by []
The Items stored in a dictionary are Unordered , while the items in a list are ordered4.What happens if you try to access spam ['foo'] if spam is {'bar':100} ?
sol:
 we will get a keyError KeyError: 'foo'5.if a dictionary is stored in spam,what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys() ?
sol:
There is no difference . The operator checks whether a value exits as a key in the dictionary or not6.if a dictionary is stored in spam,what is the difference between the expressions 'cat' in spam and 'cat' in spam.values() ?
sol:
cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.7.what is a shortcut for the following code ?
if 'color' not in spam: spam['color'] ='black'
sol:
spam.setdefault('color','black')
   8.How do you 'pretty print' dictionary values using which modules and function ?
sol:
we can pretty print a dictionary using three functions
    i)  by using pprint() function of pprint module
        Note: pprint() function doesnot prettify nested dictionaries
    ii) by using dumps() method of json module
   iii) by using dumps() method of yaml module


# In[1]:


ndict = [
  {'Name': 'John', 'Age': '23', 'Residence': {'Country':'USA', 'City': 'New York'}},
  {'Name': 'Jose', 'Age': '44', 'Residence': {'Country':'Spain', 'City': 'Madrid'}},
  {'Name': 'Anne', 'Age': '29', 'Residence': {'Country':'UK', 'City': 'England'}},
  {'Name': 'Lee', 'Age': '35', 'Residence': {'Country':'Japan', 'City': 'Osaka'}}
]

print('Printing using print() function\n',ndict)
print('-'*70)
import pprint
print('Printing using pprint() funciton')
pprint.pprint(ndict)
print('-'*70)
import json
dump = json.dumps(ndict, indent=4)
print('Printing using dumps() method\n', dump)
print('-'*70)
import yaml
dump = yaml.dump(ndict)
print('Printing using dump() method\n', dump)


# In[ ]:




