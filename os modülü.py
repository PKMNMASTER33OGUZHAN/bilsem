import os
print(os.getcwd())#dosyamızın yolunu verir.
print(os.listdir())#klasörün içindeki list tipine verir
for i in os.listdir():#listenin elemanlarına tek tek ulaşmak için
    print(i)