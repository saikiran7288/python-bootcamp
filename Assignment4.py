#!/usr/bin/env python
# coding: utf-8
1.What exactly is [ ]?
sol:
 The empty list represented by [] is a list that contains no items. This is similar to '' which represents an empty string2.In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
sol:
spam[2] = "hello"

Ex:

spam = [1,2,3,4]
spam[2] = "hello"
print(spam)
output:
[2, 4, 6, 8, 10]
[2, 4, 'hello', 8, 10]3. What is the value of spam[int(int('3'*2)//11)] ?
Sol:
'd' (Note that '3' * 2 is the string '33', which is passed to int() before being divided by 11. 
This eventually evaluates to 3, spam[3] is equal to d.)

Ex:

spam = ["a","b","c","d"]
print("spam[int(int("3"*2)//11)] ->",spam[int(int("3"*2)//11)])
output:
spam[int(int('3'*2)//11)] -> d4. What is the value of spam[-1]?
sol:
"d"  (Lists support Negative indexing, Hence spam[-1] returs 'd')

Ex:
spam = ["a","b","c","d"]
print(spam[-1])
output:
spam[-1] ->  d5. What is the value of spam[:2]?
sol: 
spam[:2] returns all elements in the list spam from 0 to 2 excluding 2
Ex:
print(spam)
print(spam[:2])
output:
['a', 'b', 'c', 'd']
['a', 'b']6. What is the value of bacon.index('cat')?
sol:
The value of bacon.index('cat') is 1 (Note: index method returns the index of first occuerence of 'cat').
ex:
bacon=[3.14,'cat',11,'cat',True]
print("bacon.index('cat') ->",bacon.index('cat'))
output:
bacon.index('cat') -> 17. How does bacon.append(99) change the look of the list value in bacon?
sol:
The append method adds new elements to the end of the list
ex:
 print(bacon)
bacon.append(99) # appends 99 to the end of the list
print(bacon)
output:
[3.14, 'cat', 11, 'cat', True]
[3.14, 'cat', 11, 'cat', True, 99]8. How does bacon.remove('cat') change the look of the list in bacon?
sol:
The remove method removes the first occurence of the element in the list
ex:
print(bacon)
bacon.remove('cat')
print(bacon)

output:
[3.14, 'cat', 11, 'cat', True, 99]
[3.14, 11, 'cat', True, 99]9.what are the list concatenation and list replication operations?
sol:
The operator for list concatenation is +, while the operator for replication is *. (This is the same as for strings.)

ex:

list_1 = ['ML','DL','AI','CV','NLP']
list_2 = ['RNN','CNN','SVN']
print(list_1 + list_2) # List Concatenation
print(list_2*2) # List Replication

output:
['ML', 'DL', 'AI', 'CV', 'NLP', 'RNN', 'CNN', 'SVN']
['RNN', 'CNN', 'SVN', 'RNN', 'CNN', 'SVN']10.what is the difference between the list method append() and insert()?
sol:
 While append() will add values only to the end of a list, insert() can add them anywhere in the list.
 
 ex:
 list = [1,2,3,4,5]
list.append(6)
print(list)
list.insert(2,'Demo')
print(list)

output:
[1, 2, 3, 4, 5, 6]
[1, 2, 'Demo', 3, 4, 5, 6]11. What are the two methods for removing items from a list?
sol:
The del statement and the remove() method are two ways to remove values from a list
12. Describe how list values and string values are identical.
sol:
Both lists and strings can be passed to len() function, have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.
13. What's the difference between tuples and lists?
sol:
Lists are Mutable, Indexable and Slicable. they can have values added, removed, or changed.
Tuples are Immutable but Indexable and Slicable. the tuple values cannot be changed at all. Also, tuples are represented using parentheses, (), while lists use the square brackets, [].
14. How do you type a tuple value that only contains the integer 42?
sol:
(42,) (The trailing comma is mandatory. otherwise its considered as a int by python Interpreter)

ex:
tup1 = (12)
tup2 = (12,)
print(type(tup1))
print(type(tup2))
output:
int
tuple15. How do you get a list value's tuple form? How do you get a tuple value's list form?
sol:
The tuple() and list() functions, respectively are used to convert a list to tuple and vice versa
16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
sol:
They contain references to list values.
17. How do you distinguish between copy.copy() and copy.deepcopy()?
sol:
The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.
