
# coding: utf-8

# In[1]:

#adres  http://matplotlib.org/users/image_tutorial.html
#Bu adrestende örnekleri inceleyebilirsiniz


# In[2]:

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#degisken img(min,max)
#inverce alacagiz


# In[3]:

img=mpimg.imread(r'C:\Users\Asus\Desktop\stinkbug.png')


# In[4]:

img.ndim


# In[5]:

img.shape


# In[6]:

plt.imshow(img)
plt.show()#yüzde 50 kırpılmış halidir


# In[7]:

img[:,100,:].max()#1.kolondaki butun renlerin max i


# In[8]:

img_1=img[1:375:2,:,:]#butun rgb yi al 2 ser artarak


# In[9]:

img_1=img[:,1:500:2,:]


# In[10]:

plt.subplot(1,2,1),plt.imshow(img)
plt.subplot(1,2,2),plt.imshow(img_1)
#plt.imshow(img_1)
plt.show()


# In[11]:

img.ndim,img.shape


# In[12]:

img_20=np.zeros((500,375,3))# boyutlarında img_20 adında matris oluşturur. Matris boyutları transpozesinde simetrik olacak
img_20.shape


# In[13]:

#3 tane rgb var her hucreye erismek icin o anki pixelin butun renklerini aldim
#for i in range(375):
    #for j in range(500):
        #img_20[j,i,:]=img(i,j,:)#img isimli 3 boyutlu kubun transpozu
        #print(img[i,j,:])for i in range(375):


# In[14]:

for i in range(375):
    for j in range(500):
        img_20[j,i,:]=img[i,j,:]


# In[15]:

plt.subplot(1,2,1),plt.imshow(img)
plt.subplot(1,2,2),plt.imshow(img_20)
#plt.imshow(img_1)
plt.show()


# In[16]:

img_30=np.zeros((500,375,3))
img_30.shape
for i in range(375):
    for j in range(500):
        img_30[j,i,:]=1-img[i,j,:]#img isimli 3 boyutlu kubun transpozu
        #img[i,j,:]

img_40=np.zeros((375,500,3))
img_40.shape
for i in range(375):
    for j in range(500):
        img_40[375-i-1,500-j-1,:]=1-img[i,j,:]
img_50=np.zeros((375,500,3))
img_50.shape
for i in range(375):
    for j in range(500):
        img_50[375-i-1,j,:]=1-img[i,j,:]
plt.subplot(2,3,1),plt.imshow(img)
plt.subplot(2,3,2),plt.imshow(img_20)
plt.subplot(2,3,3),plt.imshow(img_30)
plt.subplot(2,3,4),plt.imshow(img_30)
plt.subplot(2,3,5),plt.imshow(img_40)
plt.subplot(2,3,5),plt.imshow(img_50)
plt.show()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



