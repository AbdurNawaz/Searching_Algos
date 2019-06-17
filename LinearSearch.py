#!/usr/bin/env python
# coding: utf-8

# In[10]:


def LinearSearch(A, k):
    position = 0
    flag = False
    while position < len(A) and not flag:
        if A[position] == k:
            flag = True
        else:
            position +=1
    return flag, position

A = [45, 65, 67,23,645,23,75,23,65,98,5,34,23,657,879,43,1,34,67,98,0,2,12]

k = int(input("Please enter a number to search: "))

flag, pos = LinearSearch(A, k)
if flag == True:
    print("%d is found at position %d" % (A[pos], pos))
    
else:
    print("%d is not found" % (k))
    
import time
time.sleep(3)  


# In[ ]:




