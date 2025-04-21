# QR code encoder / decoder Python Project
# In this Code With Tomi tutorial, you will learn how to create your own QR codes 
# and encode/decode information from them. This project uses the qrcode library.

import qrcode

def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)  # File ko save karna
    print(f"QR Code '{filename}' ke naam se save ho gaya hai.")

# Example usage
generate_qr("Mubashir516", "my_qrcode.png")


import cv2

def decode_qr(image_path):
    img = cv2.imread(image_path)  # Image read karo
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        print(f"Decoded Data: {data}")
    else:
        print("No QR Code detected.")

# Example usage
decode_qr("my_qrcode.png")  # Apni QR code image ka naam likho

