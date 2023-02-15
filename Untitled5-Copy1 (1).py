#!/usr/bin/env python
# coding: utf-8

# # Assignment - 30th jan
# 

# ### Question no 1

# In[8]:


percentage = int(input("Enter your percentage : "))
if percentage > 90:
    print("A grade")
elif percentage <=90 and percentage > 80 :
    print("B Grade")
elif percentage <=80 and percentage < 60 :
    print("C Grade")
elif percentage < 60 :
    print("D Grade")
else :
    print("Invalid percentage")


# ### Question no 2

# In[7]:


cost_price = int(input("Enter the cost price of the bike : "))
if cost_price > 100000 :
    print(f"The Road tax will be : {cost_price*0.15}")
elif cost_price <=100000 and cost_price >50000 :
    print(f"The Road tax will be : {cost_price*0.10}")
elif cost_price < 50000 :
    print(f"The Road tax will be : {cost_price*0.05}")
else:
    print("invalid cost price")


# ### Question 3

# In[4]:


city = str(input("Enter the name of the city between Delhi, Agra and Jaipur : "))

if city == "Delhi" or city == "delhi" :
    print("Your city name is Delhi")
    print("monument of your city is Red Fort")
elif city == "Agra" or city == "agra" :
    print("Your city name is Agra")
    print("monumnet of the city is Taj Mahal")
elif city == "Jaipur" or city == "jaipur" :
    print("Your city name is Jaipur")
    print("monument of the city is Jal Mahal")
else :
    print("invalid city")


# ### Question no 4

# In[1]:


#Program to check how many times a number can be divided by 3 before it is less than or equal to 10

num = int(input("Enter a number: "))
count = 0
while num >= 10:  
    num = num / 3  
    count += 1
print(f"The number can be divided {count} times by 3 before it is less than or equal to 10.")
    


# ### Question no 5

# A while loop in Python is used when you want to repeatedly execute a block of code
# as long as a certain condition is true.
# The basic syntax for a while loop is:
#     while condition:
#         #code to be executed
# The code inside the loop will be executed as long as the condition is True. When the condition becomes False, the loop will stop and the program will continue to run the code after the loop.
# 
# Here's an example that demonstrates the use of a while loop:

# In[5]:


counter = 1

while counter <= 5:
    print("Counter:", counter)
    counter += 1


# ### Question no 6

# In[6]:


# Pattern 1: Triangular Number Pattern

n = int(input("Enter number of rows: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()
    i += 1

# Pattern 2: Right-angled Triangle Pattern

n = int(input("Enter number of rows: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 1

# Pattern 3: Pyramid Pattern

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(end=' ')
    for j in range(i):
        print('*', end=' ')
    print()


# ### Question no 7

# In[13]:


num = 10
while num >=1:
    print(num)
    num = num - 1


# ### Question no 8 ( same as question no 7)

# In[14]:


num = 10
while num >=1:
    print(num)
    num = num - 1


# ### Thank you

# In[ ]:





# In[ ]:





# In[ ]:




