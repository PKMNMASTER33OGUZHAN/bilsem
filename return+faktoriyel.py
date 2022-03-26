def faktoriyel(nom):
    sonuc = 1
    for i in range(1,nom+1):
        sonuc = sonuc*i
    return sonuc
sayi = int(input("sayı girin: "))
print(faktoriyel(sayi))