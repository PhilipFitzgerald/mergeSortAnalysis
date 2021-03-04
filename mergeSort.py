#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import matplotlib.pyplot as plt
import math
import numpy as np 
import pandas as pd


# In[2]:


def mergeSort(arr):
    counter =0;
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
        
        # Dividing the array elements
        L = arr[:mid]
        counter += 1;

        # into 2 halves
        R = arr[mid:]
        counter += 1;

        # Sorting first half
        mergeSort(L)
        counter += 1;

        # Sorting  second half
        mergeSort(R)
        counter += 1;

        i = j = k = 0

        # Copy data to temp arrays 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                counter += 1;
                i += 1
            else:
                arr[k] = R[j]
                counter += 1;
                j += 1
            k += 1
 
        # if any element was left
        while i < len(L):
            arr[k] = L[i]
            counter += 1;
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            counter += 1;
            j += 1
            k += 1
    return counter


# In[3]:


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# In[4]:


def addToList(listValues, size):
    for i in range(size):
        listValues.append(random.randint(1,100))


# In[5]:


listValues=[]
x = [] #sizes of inputs
y = [] # actual steps for inputs
temp=[]
expectedTable=[] #expected steps for inputs
listSizes=[10,20,30,40,50,60,70,80,90,100]
listTable=[]
size=0;
sizeCounter = 0 #tracking acceptable sizes
sets =10 #counter for while loop for number of sets iterated through
while sets > 0:
    size = listSizes[sizeCounter]
    addToList(listValues,size)
    print("Unsorted array is", end="\n")
    printList(listValues)
    counts = mergeSort(listValues)
    x.append(size) #size of input
    y.append(counts) # number of steps it took
    expectedTable.append(size*math.log(size,2)) #expected number of steps
    temp.append(size)
    temp.append(counts)
    temp.append(size*math.log(size,2))
    listTable.append(temp[:])
    temp.clear()
    print("Sorted array is: ", end="\n")
    printList(listValues)
    print("\n")
    listValues.clear()
    sizeCounter +=1
    sets-=1;


# In[6]:


plt.plot(x,y)
plt.plot(x,expectedTable)
plt.xlabel("Input data #s")
plt.ylabel("Steps count")
plt.show()


# In[7]:



df = pd.DataFrame(listTable, columns=['N', 'Steps', 'Worst Case'])
print(df)
