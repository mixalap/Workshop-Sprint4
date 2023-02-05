#!/usr/bin/env python
# coding: utf-8

# In[4]:


for num in range(1, 101):
    val = ''
    if num == 15:
        breakpoint()
    if num % 3 == 0:
        val += 'Fizz'
    if num % 5 == 0:
        val += 'Buzz'
    if not val:
        val = str(num)
    print(val)


# In[5]:


import sys
sys.version_info


# In[ ]:




