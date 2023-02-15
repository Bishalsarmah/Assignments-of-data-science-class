#!/usr/bin/env python
# coding: utf-8

# # Assignment 02-02-2023

# ### Questiopn no 1

# ### 1) Ans-  The charactertics of tuple are following -
# Ordered: Tuples maintain the order of elements in which they are defined. The first element is at index 0, the second at index 1, and so on.
# 
# a)Immutable: Once a tuple is created, you cannot modify its contents. This means you cannot add, remove, or change elements.
# 
# b)Heterogeneous: Tuples can contain elements of different data types, such as strings, numbers, and other tuples.
# 
# c)Iterable: You can loop through the elements of a tuple using a for loop or a while loop.
# 
# d)Hashable: Tuples are hashable, which means they can be used as dictionary keys.
# 
# e)Indexing and slicing: You can access individual elements of a tuple using indexing and slicing, just like with lists.
# 
# f)Parentheses: Tuples are created using parentheses ( ) instead of square brackets [ ] that are used for lists.

# ### Yes , Tuples are immutable

# In[ ]:





# ### 2) Ans- The two methods are -
# ### a)  count( )
# This method returns the number of times a particular item occurred in the tuple. ex-

# In[4]:


my_tuple = (1, 2, 3, 2, 4, 2)
count_twos = my_tuple.count(2)
print(count_twos) 


# ### b) Index() - 
# This method returns the index position of the item located inside the tuple object. ex-

# In[3]:


my_tuple = (1, 2, 3, 2, 4, 2)
index_of_two = my_tuple.index(2)
print(index_of_two)  


# The reason why tuples have only two built-in functions in Python as compared to lists is because tuples are immutable and their use cases are typically more straightforward and limited than lists. 
# 
# Lists, on the other hand, are mutable and designed for more complex data manipulation tasks, so they have more built-in methods to support those tasks

# In[ ]:





# ### Question no 3)
# Ans- The collection data type that does not allow duplicate items is the set

# In[ ]:


# Given the list[1,1,1,2,1,3,1,4,2,1,2,2,2,3,2,4,3,1,3,2,3,3,3,4,4,1,4,2,4,3,4,4]


# In[8]:


list = [1,1,1,2,1,3,1,4,2,1,2,2,2,3,2,4,3,1,3,2,3,3,3,4,4,1,4,2,4,3,4,4] 
my_set = set(list)
print(my_set)


# In[ ]:





# ### Question no 4) ans-

# In[ ]:


The union() method returns a new set that contains all the unique elements from both sets. Example-


# In[15]:


set1 = {1,2,3,4}
set2 = {4,5,6}
set3 = set1.union(set2)
print(set3)


# The update() method, on the other hand, modifies the original set by adding all the unique elements from another set or any iterable object

# In[17]:


set1 = {1,2,3,4}
set2 = {4,5,6}
set1.update(set2)
print(set1)


# In[ ]:





# ### Question no 5) Ans-

# A dictionary is an unordered collection of key-value pairs. Each key in a dictionary is associated with a value, and you can use the key to access the corresponding value. Example -
# 

# In[45]:


dict6 = {"course_name" : "Masters in data science","name" : "XYZ"}


# In[46]:


dict6


# In Python 3.7 and later versions, dictionaries are guaranteed to maintain the order of the key-value pairs as they were inserted. This means that if you iterate over the keys or values of a dictionary, they will be returned in the same order as they were added.

# In[ ]:





# ### Question no 6) Ans-

# In[ ]:


Yes , we can create nested dictionaries in python . Example-


# In[52]:


dict6 = {"key" : {"course_name" : "data science masters" , "Roll_No" : 1254}}


# In[53]:


dict6


# In[ ]:





# ### Question no 7) Ans-

# In[55]:


dict2 = {"language" : "python" , "course" : "Data Science Masters"}
dict1.setdefault("topics",["python","Machine learning","Deep learning"])


# In[56]:


dict2


# In[ ]:





# ### Question no 8) Ans-

# dict_keys object: This object contains a view of the keys in the dictionary.
# 
# dict_values object: This object contains a view of the values in the dictionary.
# 
# dict_items object: This object contains a view of the (key, value) pairs in the dictionary.

# ##### Given the Dictionary - 
# dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}

# In[60]:


dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}


# In[61]:


dict1


# In[ ]:


#dict_keys objects


# In[62]:


keys = dict1.keys()
print(f"keys: {keys}")


# In[ ]:


#dict_values Objects


# In[63]:


values = dict1.values()
print(f"values : {values}")


# In[ ]:


#dict_items objects


# In[64]:


items = dict1.items()
print(f"items : {items}")


# ### Thank you
# 

# In[ ]:




