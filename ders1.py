
# coding: utf-8

# In[13]:

a=10
print(a)


# In[14]:

import math
def findDistance(x,y):
    return math.sqrt(
    (x[0]-y[0])**2
    +
    (x[1]-y[1])**2)


# In[15]:

d=findDistance([3,0],[0,4])
d


# In[16]:

from scipy import ndimage
from scipy import misc
f=misc.face()
import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()


# In[17]:

f.ndim


# In[18]:

type(f)


# In[19]:

f[:,:,2]=0.0
plt.imshow(f)
plt.show()


# In[20]:

f.shape


# In[21]:

type(f.shape)


# In[22]:

im_size=f.shape
im_size[0]


# In[23]:

center=[im_size[0]/2,im_size[1]/2]


# In[24]:

for i in range(im_size[0]):
    for j in range(im_size[1]):
        if (findDistance([i,j],center)>100):
            f[i,j,:]=0
plt.imshow(f)
plt.show()


# In[ ]:




# In[ ]:




# In[ ]:



