#!/usr/bin/env python
# coding: utf-8

# In[13]:


listA = []
# input number of sms
n = int(input("Enter number of sms : "))
res=[]
for i in range(0, n):
    elm = (input())
    listA.append(elm) # adding the element
for j in listA:
    if j not in res:
        res.append(j)
print ("after removing duplicates sms : ",res)


# In[ ]:




