#kendisini gönderen sayıların faktöriyelini bulun
def faktoriyel(nun):
    sonuc=1
    for i in range(1,nun+1):
        sonuc=sonuc*i
        print(sonuc)
sayı=int(input("sayi giriniz"))
faktoriyel(sayı)