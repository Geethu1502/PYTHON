#!/usr/bin/env python
# coding: utf-8

# In[2]:


r=float(input("enter the radius of a circle:"))
print(r)
a=3.14*r*r
print("the area of the circle is ",a)


# In[3]:


filename=input("enter the filename:")
f_extns=filename.split(".")
print("the extension of the fine name is:" + repr(f_extns[-1]))

