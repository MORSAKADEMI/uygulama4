# 1-  "Samsung S5,Samsung S6,Samsung S7,Samsung S8" elemanlarına sahip bir liste oluşturunuz.
liste = ["Samsung S5","Samsung S6","Samsung S7","Samsung S8"]
# 2-  Liste Kaç elemanlıdır ?
print(len(liste))
# 3-  Listenin ilk ve son elemanı nedir ?
print(liste[0])
print(liste[-1])
# 4-  "Samsung S5" değerini "Samsung S9" ile değiştirin.
# telefonlar[0] = "Samsung S9"
liste[0] = "Samsung S9"
print(liste)
# 5-  "Samsung S6" listenin bir elemanı mıdır ?
if "Samsung S6" in liste:
      print("Listenin elemanıdır.")
# 6-  Listenin -3 indeksindeki değer nedir ?
print(liste[-3])
# 7-  Listenin ilk 2 elemanını alın.
print(liste[0:2])
# 8-  Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin.
del(liste[-2:])
liste += ["Samsung S9","Samsung S10"]
print(liste)
# 9-  Listenin üzerine "IPhone X" ve "IPhone XR" değerlerini ekleyin.
liste += ["IPhone X", "IPhone XR"]
print(liste)
# 10- Listenin son elemanını silin.
del liste[3]
print(liste)
# 11- Liste elemanlarını tersten yazdırınız.
liste.reverse()
print(liste)
# 12- Aşağıdaki verileri bir liste içinde saklayınız. 
       #kullaniciA: Yiğit Bilgi 2010, (70,60,70)
       #kullaniciB: Sena Turan  1999, (80,80,70)
       #kullaniciC: Ahmet Turan 1998, (80,70,90) 
yigitbilgi2010 = [70,60,70]
senaturan1999 = [80,80,70]
ahmetturan1998 = [80,70,90]
liste2 = [yigitbilgi2010,senaturan1999,ahmetturan1998]
print(liste2)
# 13- Liste elemanlarını ekrana yazdırınız.
for x in liste:
    print(x)