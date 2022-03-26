#sadece txt uzantılı dosyaları ekrana yazdırınız
import os
print(os.getcwd())
os.listdir()
for i in os.listdir():
    #if ".txt" in i:
        #print(i)
        if i.endswith(".txt"):#kelimenin sonunda .txt var isetrue döner
           print(i)