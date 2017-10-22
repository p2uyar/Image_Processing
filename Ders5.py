
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# In[4]:


pwd


# In[5]:


img_1=plt.imread(r"C:\Users\Asus\goruntuIsleme\kopek.jpg")


# In[6]:


img_1.ndim


# In[7]:


img_1.shape


# In[8]:


img_2 = img_1[1:513:2,1:763:2]
img_2.ndim,img_2.shape


# In[9]:


plt.imshow(img_2)
plt.show()
img_2


# In[10]:


img_3=np.zeros((img_2.shape[0:2]))
img_3.shape


# In[12]:


img_4=np.zeros((img_2.shape[0:2]))
img_4.shape


# In[13]:


for i in range(img_2.shape[0]):
    for j in range (img_2.shape[1]):
        n=img_2[i,j,0]/3+img_2[i,j,1]/3+img_2[i,j,2]/3
        img_3[i,j]=n
        if n>100:
            img_4[i,j]=255
        else:
            img_4[i,j]=0
        
img_3.shape


# In[14]:


plt.imshow(img_3,plt.cm.gray)
plt.show()


# In[15]:


for i in range(img_2.shape[0]):
    for j in range (img_2.shape[1]):
        n=img_2[i,j,0]/3+img_2[i,j,1]/3+img_2[i,j,2]/3
        img_3[i,j]=n
        if n>100:
            img_4[i,j]=255
        else:
            img_4[i,j]=0
        
img_3.shape


# In[16]:


plt.imshow(img_4,plt.cm.gray)
plt.show()


# In[17]:


threshold=100
for i in range(img_2.shape[0]):
    for j in range (img_2.shape[1]):
        n=img_2[i,j,0]/3+img_2[i,j,1]/3+img_2[i,j,2]/3
        img_3[i,j]=n
        if n>threshold:
            img_4[i,j]=255
        else:
            img_4[i,j]=0
plt.subplot(1,3,1),plt.imshow(img_2)
plt.subplot(1,3,2),plt.imshow(img_3,plt.cm.gray)
plt.subplot(1,3,3),plt.imshow(img_4,plt.cm.binary)
plt.imshow(img_4,plt.cm.binary)
plt.show()


# In[18]:


img_5=plt.imread(r"C:\Users\Asus\goruntuIsleme\35KSK35.jpg")


# In[19]:


img_5.ndim
img_5.shape
img_6=img_5[1:768:2,1:1024:2]
img_6.ndim, img_6.shape
plt.imshow(img_6)
plt.show()


# In[20]:


img_7=np.zeros((img_6.shape[0:2]))
img_7.shape
img_8=np.zeros((img_6.shape[0:2]))
img_8.shape


# In[24]:


for i in range(img_6.shape[0]):
    for j in range(img_6.shape[1]):
        n=img_6[i,j,0]/3+img_6[i,j,1]/3+img_6[i,j,2]/3
        img_7[i,j]=n
        if n>100:
            img_8[i,j]=255
        else:
            img_8[i,j]=0
plt.subplot(1,2,1), plt.imshow(img_6)
plt.subplot(1,2,2), plt.imshow(img_7,plt.cm.binary)
plt.show()

