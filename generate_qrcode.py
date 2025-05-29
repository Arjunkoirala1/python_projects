import qrcode

code = input('enter the url or qr code: ').strip()
file = input('enter name of the file to be saved with: ').strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(code)
image = qr.make_image(fill_color='black', back_color='white')
image.save(file)
print(f"The image saved as{file}")
