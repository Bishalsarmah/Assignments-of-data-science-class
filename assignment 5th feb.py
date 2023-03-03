#!/usr/bin/env python
# coding: utf-8

# ## Assignment 5th feb
# 

# ### Question no 1 ans -
# In Object-Oriented Programming (OOP), a class is a blueprint or a template for creating objects that share common attributes and behaviors. It defines the properties and methods that an object can have, and serves as a blueprint for creating instances of the class. An object, on the other hand, is an instance of a class that has its own unique set of properties and behaviors.
# 
# For example, consider a class called "Car". This class could have properties such as "make", "model", "color", "year", and "mileage", as well as methods such as "accelerate", "brake", and "turn". These properties and methods define the characteristics and behaviors of a car.

# In[ ]:





# ### Question no 2 ans-
# The four pillars of OOP's are -
# 
# 1)Inheritance
# 
# 2)Polymorphism
# 
# 3)Abstraction
# 
# 4)Encapsulation

# ### Question no 3 ans-
# The __init__() function is a special method in Python classes that is used to initialize the object's attributes when the object is created. It is automatically called when an object is instantiated, and it can be used to set the initial values of an object's attributes.Example-  

# In[2]:


class pwskills1:
    
    def __init__(self ,phone_number , email_id, student_id ):
        
        self.phone_number = phone_number
        self.email_id = email_id
        self.student_id = student_id
        
    
    def return_student_detials(self):
        return self.phone_number, self.email_id , self.student_id


# In[6]:


Rohan = pwskills1(8855223366,"Rohan@gmail.com",111)


# In[12]:


Rohan.phone_number


# In[16]:


Rohan.return_student_detials()


# In[ ]:





# ### Question no 4 ans-
# In Object-Oriented Programming (OOP), self is a special keyword that is used to refer to the instance of a class. It is used to access and modify the attributes and methods of an object within the class.
# 
# Self is the first parameter of instance methods, which are functions defined within a class that can be called on an object of that class. When a method is called on an object, the object is automatically passed as the self argument to the method.

# In[ ]:





# ### Question no 5 ans-

# Inheritance is a concept in Object-Oriented Programming (OOP) that allows a new class to be based on an existing class. The new class, known as the child class or subclass, inherits the properties and methods of the existing class, known as the parent class or superclass. This allows the child class to reuse code from the parent class and add new functionality as needed.
# 
# Single Inheritance: In single inheritance, a subclass inherits properties and behavior from a single parent class. This is the most common type of inheritance used in Python.
# 
# Multiple Inheritance: In multiple inheritance, a subclass inherits properties and behavior from more than one parent class.
# 
# Multi-level Inheritance: In multi-level inheritance, a subclass inherits properties and behavior from a parent class, which in turn, inherits properties and behavior from its own parent class.
