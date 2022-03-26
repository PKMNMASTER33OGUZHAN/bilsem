def bilgilerigoster(ad,soyad,no,adres="adres yok",tel="numara yok"):
    print("Adınız:",ad)
    print("Soyadınız:",soyad)
    print("NO:",no)
    print("ADresiniz:",adres)
    print("telefonunuz:",tel)
name=input("adınızı giriniz:")
surname=input("soyadınızı giriniz:")
number=input("nonuzu girin:")
adress=input()
telephone=input()
#fonksiyon eğer 5 parametre alıyor ve gönderilmeyen değere default bir değer alıyorsa fonksiyona göndemek aşağıdaki gibi yapılır
bilgilerigoster(ad=name,soyad=surname,no=number)