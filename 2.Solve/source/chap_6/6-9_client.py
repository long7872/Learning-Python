import xmlrpc.client
from PIL import Image
import base64
import io

HOST = '127.0.0.1'
PORT = 8000
with xmlrpc.client.ServerProxy(f"http://{HOST}:{PORT}/") as proxy:
    print("Merge two image ")
    a = input("Enter path of first image: ")
    b = input("Enter path of second image: ")
    print("Show Image: ")
    img_str = proxy.merge_image(a,b)
    img_byte64 = base64.b64decode(img_str)
    img_stream = io.BytesIO(img_byte64)
    img = Image.open(img_stream)
    img.show()