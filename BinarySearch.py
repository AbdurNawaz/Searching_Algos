#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def BinarySearch(A, k):
    flag = False
    low = 0
    high = len(A) - 1
    while low < high and not flag: 
        mid = int((low + high)/2)
        if A[mid] == k :
            flag = True
        
        elif k < A[mid] :
            high = mid - 1
            
        else :
            low = mid + 1
    return flag, mid

A = [456,342,5,45,87,23,54,6,78,9,6754,32,12,34]
A = sorted(A)
k = int(input("Please enter a number to search: "))
flag, pos = BinarySearch(A, k)
if flag == True:
    print("%d is fount at position %d" % (A[pos], pos))
else:
    print("%d is not found"%(k))

import time
time.sleep(3)

# In[ ]:




