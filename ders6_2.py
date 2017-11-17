
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img_a1=mpimg.imread('a1.jpg')
img_a2=mpimg.imread('a2.jpg')
img_a3=mpimg.imread('a3.jpg')
img_a4=mpimg.imread('a4.jpg')
img_a5=mpimg.imread('a5.jpg')

img_b1=mpimg.imread('b1.jpg')
img_b2=mpimg.imread('b2.jpg')
img_b3=mpimg.imread('b3.jpg')
img_b4=mpimg.imread('b4.jpg')
img_b5=mpimg.imread('b5.jpg')

img_c1=mpimg.imread('c1.jpg')
img_c2=mpimg.imread('c2.jpg')
img_c3=mpimg.imread('c3.jpg')
img_c4=mpimg.imread('c4.jpg')
img_c5=mpimg.imread('c5.jpg')

img_d1=mpimg.imread('d1.jpg')
img_d2=mpimg.imread('d2.jpg')
img_d3=mpimg.imread('d3.jpg')
img_d4=mpimg.imread('d4.jpg')
img_d5=mpimg.imread('d5.jpg')

img_e1=mpimg.imread('e1.jpg')
img_e2=mpimg.imread('e2.jpg')
img_e3=mpimg.imread('e3.jpg')
img_e4=mpimg.imread('e4.jpg')
img_e5=mpimg.imread('e5.jpg')


# In[4]:


#ayn boyutlarda bir resim daha oluturuyoruz

img_a11=img_a1
img_a12=img_a2
img_a13=img_a3
img_a14=img_a4
img_a15=img_a5

img_b11=img_b1
img_b12=img_b2
img_b13=img_b3
img_b14=img_b4
img_b15=img_b5

img_c11=img_c1
img_c12=img_c2
img_c13=img_c3
img_c14=img_c4
img_c15=img_c5

img_d11=img_d1
img_d12=img_d2
img_d13=img_d3
img_d14=img_d4
img_d15=img_d5

img_e11=img_e1
img_e12=img_e2
img_e13=img_e3
img_e14=img_e4
img_e15=img_e5
plt.imshow(img_a12)
plt.show()
plt.imshow(img_a12)
plt.show()
plt.imshow(img_a12)
plt.show()
plt.imshow(img_a12)
plt.show()
plt.imshow(img_a12)
plt.show()


# In[7]:


threshold=12 #ortalama deger belirledik bundan asag olanlar 0 yukar olanlar 1 yapcaz

for i in range(img_a1.shape[0]):
    for j in range(img_a1.shape[1]):
        n=img_a12[i,j]=img_a1[i,j,0]/3+img_a1[i,j,1]/3+img_a1[i,j,2]/3
        img_a12[i,j]=n #fotoyu griye çevirdik
        #şimdi fotoyu griden siyah beyaza ceviricez
        if n>threshold: #n threshold değerinden büyükse
            img_a12[i,j]=255 #img ye 255 degerini ata
        else:
            img_a12[i,j]=0 #degilse img ye 0 degerini ata


# In[6]:


plt.imshow(img_a12,plt.cm.binary)
plt.show()


# In[8]:


def bwCevirme(img1,img2):
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            n=img2[i,j]=img1[i,j,0]/3+img1[i,j,1]/3+img1[i,j,2]/3
            img2[i,j]=n #fotoyu griye çevirdik
            #şimdi fotoyu griden siyah beyaza ceviricez
            if n>threshold: #n threshold değerinden büyükse
                img2[i,j]=255 #img ye 255 degerini ata
            else:
                img2[i,j]=0 #degilse img ye 0 degerini ata


# In[ ]:


defbwCevirme()

