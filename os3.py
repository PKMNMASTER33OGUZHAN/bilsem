import os
for kökdizin,altdizin,dosyalar in os.walk("c:\\"):
    for dosya in dosyalar:
        print(dosya)