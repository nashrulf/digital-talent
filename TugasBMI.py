#!/usr/bin/env python
# coding: utf-8

# # Latihan
# Body Mass Index (BMI) menentukan sebuah keidealan berat badan terhadap tinggi badan. 
# Berikut adalah formula dari BMI : BMI = weight (kg) ÷ height^2 (m^2)
# 
# Berikut adalah kategorisasi BMI
# 
# ![](Pictures/kategori.png)
# 
# Buatlah sebuah program yang memiliki dua variabel berat badan dengan satuan KG, dan tinggi badan dengan satuan CM, kemudian keluaran dari program adalah Kategori BMI

# Jawaban :

# In[26]:


#Perhitungan Ideal Berat Badan
BB = 50
TB = 170
BMI = BB / ((TB/100)**2)
print ("Berat Badan yang anda masukkan",BB,"KG")
print ("Tinggi Badan yang anda masukkan",TB,"CM")
print ("Body Mass Index (BMI) Anda",BMI)

if BMI<0:
    print("Anda belum memasukkan berat badan atau tinggi badan")
elif BMI<15:
    print("Very severely underweight")
elif BMI<16:
    print("Severely underweight")
elif BMI<18.5:
    print("Underweight")
elif BMI<25:
    print("Normal (healthy weight)")
elif BMI<30:
    print("Overweight")
elif BMI<35:
    print("Moderately obese")
elif BMI<40:
    print("Severely obese")
elif BMI>40:
    print("Very severely obese")
else:
    print("Selesai")


# In[ ]:




