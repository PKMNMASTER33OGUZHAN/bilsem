#bir text dosyasına birden bine kadar sayıları yazdırın
dosya=open("sayilar.txt","w",encoding="utf-8")
for i in range(1000):
    dosya.write(str(i)+"\n")
dosya.close()