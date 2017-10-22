
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

myList=[0,1,2,3,4,5]


# In[ ]:

def createList(size):
    myList=[]
    for i in range(size):
        myList.append(i)
    return myList
def listIncrement(l,n):
    myL=[]
    for i in range(len(l)):
        myL.append(l[i]+n)
    return myL
L_1=createList(5)
L_1
L_2=listIncrement(L_1,5)
L_2


# In[ ]:

#createList(500)
get_ipython().magic(u'timeit myL_1=listIncrement(createList(9000000),50)')


# In[ ]:

get_ipython().magic(u'timeit np.arange(9000000)+1')


# In[ ]:

size=10
my_10=np.arange(size)
my_10


# In[ ]:

my_10+1


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



