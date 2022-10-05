#!/usr/bin/env python
# coding: utf-8
1.What are the two values of the Boolean data type? How do you write them?
solution:-
boolean values
i)True  
ii)False
# In[3]:


a= 90
b= 60
bool(a>b)


# In[4]:


bool(a<b)

What are the three different types of Boolean operators?
solution:-
 there are three types of boolean operators they are:
 i)& #and
 ii)/ #or
 iii)! #not
# In[15]:


bool(a>b & a<b)


# In[16]:


bool(a>b | a<b )


# In[18]:


bool(a!=b)

3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate )

solution:-
True and True is True

True and False is False

False and True is False

False and False is False

True or True is True

True or False is True

False or True is True

False or False is False

not True is False

not False is True


Truth Table for AND
A B output
0 0 0
0 1 0
1 0 0
1 1 1

Truth Table for OR
A B output
0 0 0
0 1 1
1 0 1
1 1 1 

Truth Table for NOT

A output
01
10


# In[21]:





# In[29]:


get_ipython().set_next_input('4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')

print((5 > 4) and (3 == 5)) #False
print(not (5 > 4))#False
print((5 > 4) or (3 == 5))#True
print(not ((5 > 4) or (3 == 5)))#False
print((True and True) and (True == False))#False
print((not False) or (not True))#Ture

5. What are the six comparison operators?
 i)   >
 ii)  <
 iii) >=
 iv)  <=
 v)   ==
 vi)  !=
 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

solution:-
 == is an comparsion operator which compare two values and returns boolean value as output.where = is an asignment operator which is used to assign the values one variable to another variable.
# In[33]:


#7. Identify the three blocks in this code:
spam = 0
if spam == 10:   #block 1
    print('eggs')
if spam > 5:    #block 2
    print('bacon')
else:            #block 3
    print('ham')
    print('spam')
    print('spam')

8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
# In[37]:


spam = int(input("enter an number"))
if spam ==1:
    print("Howdy")
elif spam ==2:
    print("hii welcome")
else:
    print("nothing else!")

9.If your programme is stuck in an endless loop, what keys you’ll press?
solution:-
if an programme stuck in endless loop we will pres ctrl+c.
# In[ ]:




10. How can you tell the difference between break and continue?

# In[46]:


#use of break
for i in range(10):
    if(i==7):
        break
    print(i)
        
print("breaked")
# use of continue
for i in range(10):
    if(i== 7):
        continue
    print(i)


solution:-
The break statement will move the execution outside and just after a loop. The continue statement will move the execution to the start of the loop.11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# In[47]:


for i in range(10):
    print(i)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") 
for i in range(0,10):
    print(i)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
for i in range(0,10,1):
    print(i)

From the above output we can conclude that they all do the same thing. The range(10) call ranges from 0 up to (but not including) 10, range(0, 10) tells the loop to start at 0, and range(0, 10, 1) tells the loop to increase the variable by 1 on each iteration.12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
# In[48]:


#Use of For Loop
print("For Loop")
for i in range(1,11):
    print(i)
#Use of While Loop
print("While Loop")
a =1
while a <= 10:
    print(a)
    a+=1

13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

solution:-
 function can be called with spam.bacon().

 

