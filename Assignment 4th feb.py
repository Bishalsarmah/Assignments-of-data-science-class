#!/usr/bin/env python
# coding: utf-8

# ### Assignment 4th feb

# Question no 1 ans-

# In[19]:


lst = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]


# In[21]:


sorted(lst, key=lambda x: x[1], reverse=True)


# In[ ]:





# Question no 2 ans-

# In[1]:


lst = [1,2,3,4,5,6,7,8,9,10]


# In[6]:


list(map(lambda x : x**2, l))


# In[ ]:





# Question no 3 ans-
# 

# In[4]:


l = [1,2,3,4,5,6,7,8,9,10]


# In[5]:


tuple(map(lambda x : str(x), l))


# In[ ]:





# Question no 4 ans-

# In[9]:


l1 = range(1,25)


# In[10]:


from functools import reduce


# In[13]:


reduce(lambda x,y : x*y , l1)


# In[ ]:





# Question no 5 ans-

# In[14]:


lst =[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]


# In[16]:


list(filter(lambda x : x%2==0 and x%3==0 , lst))


# In[ ]:





# Question no 6 ans-

# In[17]:


l1 = ['python', 'php', 'aba', 'radar', 'level']


# In[18]:


list(filter(lambda x : x == x[::-1] , l1))


# In[ ]:




