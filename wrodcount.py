#!/usr/bin/env python
# coding: utf-8

# # Soal 2 - Word Count
# Diberikan sebuah paragraf, hitunglah banyak kemunculan masing-masing kata. Contoh : "Presiden pagi ini melakukan kunjungan ke Jogja"
# 
# Presiden: 1
# pagi: 1
# ini: 1
# melakukan: 1
# kunjungan: 1
# ke: 1
# Jogja: 1
# hints: Gunakan Dictionary dalam menyimpan word count. Gunakan kata sebagai key, dan jumlah kemunculan sebagai val

# In[4]:


from collections import Counter

print ("Paragraf :")
paragraf = "Barcelona berhasil merebut posisi puncak klasemen La Liga Spanyol seusai menang 4-2 atas Sevilla pada pertandingan pekan kesembilan di Stadion Camp Nou, Sabtu (20/10/2018) atau Minggu dini hari WIB. Barcelona membuka keunggulan pada menit ke-2 melalui gol yang dicetak oleh Philippe Coutinho. Lionel Messi menggandakan keunggulan Barcelona, 10 menit berselang.  Namun, nahas bagi Barcelona, karena Messi harus ditarik keluar pada menit ke-26 setelah mengalami cedera. Tanpa Messi, skor 2-0 bertahan hingga babak pertama berakhir."
print(paragraf)

# Remove unused char
paragraf = paragraf.lower()
paragraf = paragraf.replace('.', '')
paragraf = paragraf.replace(',', '')

# Convert Paragraf to list
listString = paragraf.split()

# Count each duplicate string
# singlet = Counter(listString)
singlet = {}
for row in listString:
    if row in singlet:
        singlet[row]+=1
    else:
        singlet[row] = 1

print("Jumlah:")
print("=============")
for row in singlet.items():
    print(row[0], ": ", row[1])


# In[ ]:





# In[ ]:




