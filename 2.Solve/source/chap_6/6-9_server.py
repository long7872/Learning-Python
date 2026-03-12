from xmlrpc.server import SimpleXMLRPCServer
from PIL import Image, ImageFilter, ImageEnhance
import base64
import io
import os

# Filter
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, '1_image.png')
img = Image.open(image_path)
img_smoothed = img.filter(ImageFilter.SMOOTH)
blurred = img.filter(ImageFilter.BLUR)
img_sharpenned = img.filter(ImageFilter.SHARPEN)
contoured = img.filter(ImageFilter.CONTOUR)
emboss = img.filter(ImageFilter.EMBOSS)

# img.show()
# img_smoothed.show()
# blurred.show()
# img_sharpenned.show()
# contoured.show()
# emboss.show()

# ===================================================

# Contrast
img_contrast = ImageEnhance.Contrast(img)
image_path = os.path.join(current_dir, '1_image_contrast.png')
img_contrast.enhance(2.0).save(image_path)
img_new = Image.open(image_path)

# img_new.show()

# ===================================================

# Merge
image1_path = os.path.join(current_dir, '1_image.png')
image2_path = os.path.join(current_dir, '2_image.png')
img1 = Image.open(image1_path)
img2 = Image.open(image2_path)
img1.paste(img2)

# img1.show()

# ===================================================

# Blend
image1_path = os.path.join(current_dir, '1_image.png')
image2_path = os.path.join(current_dir, 'miss.gif')
img1 = Image.open(image1_path)
img2 = Image.open(image2_path)
img3 = img1.resize((800,500))
img4 = img2.resize((800,500))
img5 = img3.convert("RGBA")
img6 = img4.convert("RGBA")
alphaBlended = Image.blend(img5, img6, alpha=.2)

# img1.show()
# img2.show()
# img3.show()
# img4.show()
# img5.show()
# img6.show()
# alphaBlended.show()

def merge_image(path1, path2):
    img1 = Image.open(path1)
    img2 = Image.open(path2)
    img1.paste(img2)
    buffer = io.BytesIO()
    img1.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()
    img_byte64 = base64.b64encode(img_bytes)
    img_str = img_byte64.decode()
    return img_str

HOST = '127.0.0.1'
PORT = 8000
server = SimpleXMLRPCServer((HOST, PORT))
print("Listen to the signal from the port 8000...")
server.register_function(merge_image)
server.serve_forever()