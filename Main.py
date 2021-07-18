import os
import Image_barcode
import camera_barcode

print("================== Barcode Scanner ==================")
print("A VivinMeth Product")
print("version: v2-beta")
loop = 1
while (loop == 1):
    print("=====================================================")
    print("Choose:\n1. Image\n2. Realtime")
    x = int(input(":"))
    if x == 1:
        print("=====================================================")
        fil = input("")
        Image_barcode.scan(fil)
    elif x == 2:
        print("=====================================================")
        camera_barcode.scan(fil)
    elif x == 3:
        print("=====================================================")
        print("Exiting Program")
        print("=====================================================")
        exit()
    else:
        print("=====================================================")
        print("Wrong input try again")
