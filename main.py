import qrcode
from pyzbar import pyzbar
from PIL import Image
#import webbrowser
#qr = qrcode.make('1') qr generator
#qr.save('qr1.png') save qr

qrcode = pyzbar.decode(Image.open('qr1.png'))
qroutput = qrcode[0].data.decode('ascii')

if qroutput == "1":
    print(qroutput)
    #webbrowser.open('https://github.com/pizmalcantara/')   
else:
    print("Okunan QR; veri tabanımızda bulunmamaktadır.")
