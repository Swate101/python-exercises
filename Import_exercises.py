#!/usr/bin/env python
# coding: utf-8

# In[2]:


import function_expy


# In[5]:


from function_expy import shout


# In[6]:


shout('hi')


# In[12]:


from function_expy import get_letter_grade, is_two, calculate_tip, is_vowel


# In[8]:


get_letter_grade (50)


# In[9]:


calculate_tip (100)


# In[10]:


function_expy.is_vowel


# In[14]:


is_vowel ('a')


# In[16]:


from function_expy import get_letter_grade as Redo


# In[18]:


Redo (50)


# In[19]:


import itertools


# In[22]:


itertools.product


# In[20]:


list(itertools.product("abc", "123"))


# In[21]:


# 9 diff way and combinations / /3 on each letter #


# In[27]:


itertools.combinations


# In[35]:


list(itertools.combinations("abcd", 2)) # ??? how do i get the len finction to work


# In[36]:


# 6 Diffrent combinations 


# In[37]:


list(itertools.permutations("abcd", 2))


# In[ ]:


# there are 12 diffrent premutations that are avliable #

