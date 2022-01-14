#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Vishu works as a personal assistant for a collector. The collector is very strict when it comes to
duplicate sms. He asks his personal assistant to delete all sms that are duplicates and to keep one
copy of each. Helo Vishu by writing a program that can tell him what sms to keep and what to
delete.
Input
1. N – number of sms
2. For each I in N:
a. Sms subject (one word no special characters)
Output
N outputs specifying whether or not to delete the message. Use ‘D’- as a prefix to delete otherwise
keep it as is
Example
N – 5
Offer
Urgent
Minister
Offer
Urgent
Output
Offer
Urgent
Minister
D-Offer
D-Urgent


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




