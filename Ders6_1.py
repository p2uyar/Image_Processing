
# coding: utf-8

# In[1]:


import math
#uzayda iki nokta arasında uzaklık
def myDistance(a,b):
    mypoint_1=a
    mypoint_2=b
    a=(myPoint_1[0]-myPoint_2[0])**2 
    b=(myPoint_1[1]-myPoint_2[1])**2
    return math.sqrt(a+b)


# In[2]:


myPoint_1=[0,0]
myPoint_2=[1,0]
myPoint_3=[0,1]
myPoint_4=[1,1]


# In[3]:


myDistance(myPoint_2,myPoint_3)


# In[4]:


a=myPoint_1[0]+myPoint_2[0]+myPoint_3[0]+myPoint_4[0]
b=myPoint_1[1]+myPoint_2[1]+myPoint_3[1]+myPoint_4[1]
center_Point=[a/4,b/4]
center_Point


# In[10]:


#4 tane noktanın orta noktasını bulma
def findCenter(List_Of_Points):
    a=0
    b=0
    for point in List_Of_Points:
        #her yeni pointle karsılastıkca a ve b degerleri
        a=a+point[0]
        b=b+point[1]
    l=len(List_Of_Points) #gelen listenin uzunlugunu al
    return[a/l,b/l] # a'yı gelen listenin uzunluguna bol


# In[11]:


myPoint_1=[0,0]
myPoint_2=[1,0]
myPoint_3=[0,1]
myPoint_4=[1,1]


# In[12]:


my_Point_List=[]
my_Point_List.append(myPoint_1)
my_Point_List.append(myPoint_2)
my_Point_List.append(myPoint_3)
my_Point_List.append(myPoint_4)
center=findCenter(my_Point_List)
center

