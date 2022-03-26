file=open("bilgiler.txt","w",encoding="utf-8")
#w:dosya oluşturur eğer dosya varsa silip tekrar oluşturur
#encoding:türkçe karakterleri okumayı sağlar
#nereye oluşturur?phyton file neredeyse oraya
file.write("merhaba hello belgesi...\n\n")
file.write("bugün halay çekmeyi öğreniyorum\n")
file.close()#açılan dosyaları kapatmak zorundayım

