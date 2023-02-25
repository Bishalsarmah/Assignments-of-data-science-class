#!/usr/bin/env python
# coding: utf-8

# ### Assignment 03 feb

# #### Question no 1 ans-

# #### 'def' keyword is used to create a function in python

# In[2]:





# In[35]:


def odd_func():
    n = []
    for i in range(1,25):
        if i%2 != 0:
            print(i)
        n.append(i)
    return n


# In[59]:


print(odd_func())
    


# #### Question no 2 ans-

# #### The *args syntax is used to pass a variable number of positional arguments to a function. It allows you to pass any number of arguments to a function, and the function will receive them as a tuple

# #### example - 

# In[61]:


def test1(*args):
    return args


# In[62]:


test1(1,2,3,4,5)


# In[ ]:





# The **kwargs syntax is used to pass a variable number of keyword arguments to a function. It allows you to pass any number of keyword arguments to a function, and the function will receive them as a dictionary

# In[63]:


#### example-


# In[64]:


def test2(**kwargs):
    return kwargs


# In[65]:


test2(a = 20 , b = 11 , c = "pwskills" , d = "data science masters")


# In[ ]:





# #### Question no 3 ans-

# ####  iterator is an object that can be iterated (looped) upon. It is used to implement a sequence of values that can be accessed one at a time.
# #### To initialize an iterator object in Python, you can use the built-in iter() function, which takes an iterable object (such as a list, tuple, or string) as its argument and returns an iterator object.

# In[66]:


my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
my_iterator = iter(my_list)

for i in range(5):
    print(next(my_iterator))


# In[ ]:





# #### Question no 4 ans-
# #### A generator function in Python is a special type of function that returns an iterator object, which can be used to generate a sequence of values on-the-fly, without having to store them in memory.
# #### In a generator function, the yield keyword is used to return a value from the function, while also preserving the state of the function so that it can be resumed later to generate the next value.

# In[69]:


def test_fib(n) :
    a,b = 0,1
    for i in range(n):
        yield a 
        a,b = b ,a+b 


# In[70]:


test_fib(10)


# In[71]:


for i in test_fib(10):
    print(i)


# In[ ]:





# #### Question no 5 ans-

# In[73]:


def generate_primes():
    primes = []
    for num in range(2, 1000):
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num


# In[74]:


prime_iterator = generate_primes()
for i in range(20):
    print(next(prime_iterator))


# In[ ]:




