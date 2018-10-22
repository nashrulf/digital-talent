#!/usr/bin/env python
# coding: utf-8

# # TUGAS ANGKA
# Diberikan sekumpulan Nilai Random antara 0 sampai dengan 100 sebanyak 250 nilai. Buatlah program untuk melakukan hal berikut:
# 1. Tampilkan Angka Ganjil dari ke 250 nilai tersebut
# 2. Tampilkan berapa banyak yang mendapatkan nilai lebih dari 70
# 3. Tampilkan standar deviasi dari sekumpulan nilai tersebut
# 4. Tampilkan nilai maksimum dan minimum
# 5. Tampilkan modus dari sekumpulan nilai tersebut

# In[13]:


import random

# GENERATE RANDOM
nilaiTugas = []
for i in range(250):
    nilaiTugas.append(random.randrange(1,100,1))

print(nilaiTugas)

# TAMPILKAN:
# ganjil
# nilai > 70
# standar deviasi
# maksimum
# minimum
# modus


# In[28]:


#Menampilkan Angka Ganjil
ganjil = []

for i in nilaiTugas:
    if i % 2 != 0:
        ganjil.append(i)
        
print("Angka Ganjil : ")
print(ganjil)


# In[20]:


#Tampilkan nilai >= 70
# moreThan70 = list(filter(lambda x: x > 70, nilaiTugas))
moreThan70 = []

for row in nilaiTugas:
    if row > 70:
        moreThan70.append(row)
        
print("nilai > 70 : ", len(moreThan70))


# In[32]:


# Menampilkan nilai maksimum
nilaiMax = 0
for nimax in nilaiTugas:
    if nimax > nilaiMax:
        nilaiMax = nimax

print("Max : ", nilaiMax)


# In[33]:


# Menampilkan nilai minimum
nilaiMin = 999
for row in nilaiTugas:
    if row < nilaiMin:
        nilaiMin = row

print("Min : ", nilaiMin)


# In[35]:


# Menampilkan nilai modus
modusList = {}
for row in nilaiTugas:
    if row in modusList:
        modusList[row]+= 1
    else:
        modusList[row] = 1

modusListSort = sorted(modusList.items(), key=lambda kv: kv[1], reverse=True)
maxCount = modusListSort[0][1]
modus = []

for row in modusListSort:
    if row[1] == maxCount:
        modus.append(str(row[0]))
    else:
        break
        
print("Modus : ", ', '.join(modus))


# In[36]:


import math
# Menampilkan standar deviasi
sumX1 = 0
sumX1Kuadrat = 0
for row in nilaiTugas:
    sumX1+= row
    sumX1Kuadrat+= (row**2)
    
standarDeviasi = math.sqrt(((len(nilaiTugas) * sumX1Kuadrat ) - (sumX1**2)) / (len(nilaiTugas) * (len(nilaiTugas) - 1)))
print("Standar Deviasi : ", standarDeviasi)


# In[ ]:




