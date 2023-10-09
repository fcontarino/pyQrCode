import wifi_qrcode_generator as qr
qr_code = qr.wifi_qrcode('WiFi 5G',False,'WPA','F3D337871645.')
qr_code.make_image().show()