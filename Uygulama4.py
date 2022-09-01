# 1-  "Samsung S5,Samsung S6,Samsung S7,Samsung S8" elemanlarına sahip bir liste oluşturunuz.
Telefonlar = ["Samsung S5","Samsung S6","Samsung S7","Samsung S8"]

# 2-  Liste Kaç elemanlıdır ?
print(len(Telefonlar))

# 3-  Listenin ilk ve son elemanı nedir ?
print(Telefonlar[0],Telefonlar[-1])

# 4-  "Samsung S5" değerini "Samsung S9" ile değiştirin.
# telefonlar[0] = "Samsung S9"
Telefonlar[0] = "Samsung S9"
print(Telefonlar)

# 5-  "Samsung S6" listenin bir elemanı mıdır ?
if "Samsung S6" in Telefonlar:
    print("True")

# 6-  Listenin -3 indeksindeki değer nedir ?
print(Telefonlar[-3])

# 7-  Listenin ilk 2 elemanını alın.
del Telefonlar[0:2]
print(Telefonlar)

# 8-  Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin.
Telefonlar[0:2] = ["Samsung S9","Samsung S10"]
print(Telefonlar)

# 9-  Listenin üzerine "IPhone X" ve "IPhone XR" değerlerini ekleyin.
Telefonlar = Telefonlar + ["IPhone X","IPhone XR"]
print(Telefonlar)

# 10- Listenin son elemanını silin.
del Telefonlar[-1]
print(Telefonlar)

# 11- Liste elemanlarını tersten yazdırınız.
print(Telefonlar[::-1])

# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # kullaniciA: Yiğit Bilgi 2010, (70,60,70)
kullaniciA = ["Yiğit", "Bilgi", "2010", "70,60,70"]
      # kullaniciB: Sena Turan  1999, (80,80,70)
kullaniciB = ["Sena", "Turan", "1999", "80,80,70"]
      # kullaniciC: Ahmet Turan 1998, (80,70,90) 
kullaniciC = ["Ahmet", "Turan", "1998", "80,70,90"]

Kullanıcılar = kullaniciA + kullaniciB + kullaniciC

# 13- Liste elemanlarını ekrana yazdırınız.
print(Kullanıcılar)

#Ekleme ve del işini ayrı yapmazsak saymıyor 