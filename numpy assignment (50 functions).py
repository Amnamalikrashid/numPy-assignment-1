#!/usr/bin/env python
# coding: utf-8

# # Function 1

# In[3]:


import numpy as np


# In[6]:


np.linspace(0,100,6)         #Array of 6 evenly divided values from 0 t 100


# In[9]:


np.linspace(10,100,10)


# # Function 2

# In[10]:


np.arange(0,10,3)           #Array of values from 0 to less than 10 with step 3


# In[11]:


np.arange(2,20,2)


# # Function 3

# In[13]:


np.identity(5)            # 5*5 array of 0 with 1 on diagonal (identity matrix)


# In[17]:


np.eye(7)


# In[ ]:





# # Function 4

# In[20]:


np.full((2*3),8)            # 2*3 array with all the values 4


# In[21]:


np.full((2,5),5) 


# # Function 5

# In[23]:


np.random.randn(2,3)*100      # 6*7 array of random floats between 0-100


# # Function 6

# In[26]:


a = np.array([3,5,7,9,18,24])
a.shape


# # Function 7

# In[27]:


len(a)


# # Function 8

# In[29]:


a.ndim


# # Function 9

# In[33]:


a.size


# # Function 10

# In[31]:


a.dtype


# In[34]:


a.dtype.name


# In[35]:


a.astype(int)


# # Function 11

# In[37]:


np.info(a)


# # Function 12

# In[45]:


np.copy(a) # copy a to a new memory


# # Function 13

# In[51]:


b = np.array([(1,2,3),(4,5,6)])       # Convert 2d array to 1d array
b.flatten()


# # Function 14

# In[52]:


b.T                 # Transposes (rows become column)


# # Function 15

# In[56]:


np.append(b,4)


# # Function 16

# In[60]:


np.insert(b,5,7)


# # Function 17

# In[63]:


x = ([1,3,5],[4,8,9])
arr1 = np.array(x)
arr1


# In[64]:


arr2 = ([5,6,7],[8,9,0])
arr2


# In[65]:


np.concatenate((arr1,arr2),axis=0) # row wise


# In[66]:


np.concatenate((arr1,arr2),axis=1) # column wise


# In[67]:


np.vstack((arr1,arr2)) # row vise


# In[68]:


np.hstack((arr1,arr2)) # column vise


# # Function 18

# In[74]:


arr2 = ([5,6,7],[8,9,0])
d = np.array(arr2)
np.split(d,[1],axis=0) # row vise


# In[75]:


arr2 = ([5,6,7],[8,9,0])
d = np.array(arr2)
np.split(d,[1],axis=1) # column vise


# In[76]:


arr2 = ([5,6,7],[8,9,0])
d = np.array(arr2)
np.hsplit(d,[1]) # column vise


#  # Function 19

# In[77]:


b.sum() # array wise sum


# # Function 20

# In[79]:


b.min() # array wise minimum value


# # Function 21

# In[80]:


b.max() # array wise maximum value


# # Function 22

# In[81]:


b.cumsum() # comulative value of all values


# # Function 23

# In[82]:


b.mean()


# # Function 24

# In[86]:


np.median(b)


# # Function 25

# In[87]:


np.std(b)        # Standard deviation


# # Function 26

# In[88]:


np.argmax(b) # returns indices of the maximum elemrnt of the array in particular axis.


# # Function 27

# In[91]:


np.argmin(b) # return indeces of the min element of the array in a particular axis


# # Function 28

# In[92]:


np.var(b) # variance


# # Function 29

# In[93]:


np.cumprod(b) # compute the comulative product of array elements over a great axis


# # Function 30

# In[94]:


a = np.array([1,2,3,4,5,6])


# In[95]:


b = np.array([7,8,9,1,2,3])


# In[96]:


a+b # Arithematic operations


# # Function 31 

# In[97]:


a-b


# # Function 32

# In[98]:


np.divide(a,b)


# # Function 33

# In[99]:


np.multiply(a,b)


# # Function 34

# In[100]:


np.exp(a)  # exponentiation


# # Function 35

# In[101]:


np.sqrt(a)


# # Function 36

# In[102]:


np.log(a)


# # Function 37

# In[105]:


np.floor(a) # compute the floor of each element


# # Function 38

# In[107]:


a = np.array([1,2.4,5.6,2.4,7,1.9])


# In[109]:


np.rint(a)     # round elements to nearest integer


# # Function 39

# In[110]:


a


# In[112]:


np.ceil(a) # smallest number greater than or equal to that number


# # Function 40 

# In[114]:


a = [0,1,2,3,2.4,-1] # Compute the sign of each element:1(positive),0(zero),or-1(negative))
np.sign(a)


# # Function 41

# In[115]:


np.abs(a)   # element wise for integer ,floating point ,or complex values


# # Function 42

# In[119]:


np.unique(a)  # compute the sorted and unique elements in a


# # Function 43

# In[121]:


np.intersect1d(a,b) # elements common in a and b


# # Function 44

# In[123]:


np.setdiff1d(a,b) # elements in a that are not in b


# # Function 45

# In[124]:


np.power(a,4)


# # Function 46

# In[143]:


a = np.array([3,4,5,6,7,8])
b = np.array([2,9,5,6,0,8])
np.in1d(a,b) # create a boolean array whether each element of x is contained in y


# # Function 47

# In[145]:


np.setxor1d(x,y) # set symmetrical differences;elements that are in either of the arrays,but not both


# # Function 48

# In[146]:


np.union1d(x,y) # compute the sorted union of elements


# # Function 49

# In[149]:


np.empty((7,7))


# # Function 50

# In[157]:


np.array([1,5,7,8])
np.repeat(d,3)
np.tile(d,2)


# In[ ]:





# In[ ]:





# In[ ]:




