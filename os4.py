import os
import shutil
#bilgi sayardaki resimleri bul kopyala
for kokklasor,altklasör,dosyalar in os.walk("C:\\Users\ogr10\Desktop\\resim\\"):
    for dosya in dosyalar:#dosyalar listenin içinde dolaş
        if dosya.endswith(".jpg"):#resim ise çalış
            shutil.copy(kokklasor+"/"+dosya,dosya)#kaynaktaki adı ne ise o olur