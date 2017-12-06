
import random
dizi=[]
for i in range(25):
 dizi.append(random.randint(0,10))
dizi.sort()
dizi.append(0)
for i in range(len(dizi)):
 if i==len(dizi)-1:
 break
 if dizi[i]!=dizi[i+1]:
 print(dizi[i]," ", dizi.count(dizi[i]),"tane vardır")
