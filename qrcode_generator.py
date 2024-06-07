
# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from PIL import Image, ImageDraw
from pyqrcode import QRCode 
  
  
# String which represents the QR code 
s : str = "Jerry loves Harry"
  

### heart shape qrcode

# Generate a QR code
url : object = pyqrcode.create(s)
url.png(r'C:\Users\harish\git\Problem_Solving\qr_code.png', scale=10)

# Create a new image with a white background
width , height = 200, 200
fill : str = 'red'
img = Image.new('RGB', (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
polygon = [
    (width / 10, height / 3),
    (width / 10, 81 * height / 120),
    (width / 2, height),
    (width - width / 10, 81 * height / 120),
    (width - width / 10, height / 3),
]
draw.polygon(polygon, fill=fill)
#img.show()

draw.ellipse((0, 0,  width / 2, 3 * height / 4), fill=fill)
draw.ellipse((width / 2, 0,  width, 3 * height / 4), fill=fill)


# Save the image
draw.save(r'C:\Users\harish\git\Problem_Solving\heart_shape.png')


# Open the heart shape image
heart_image = Image.open(r'C:\Users\harish\git\Problem_Solving\heart_shape.png')

# Resize the QR code to fit inside the heart shape
qr_code = Image.open(r'C:\Users\harish\git\Problem_Solving\qr_code.png')
qr_code.thumbnail(heart_image.size)
# qr_code_resized = qr_code.resize(heart_image.size, Image.ANTIALIAS)

# Paste the QR code onto the heart shape image
heart_image.paste(qr_code, (0, 0))

# Save the final image
heart_image.save(r'C:\Users\harish\git\Problem_Solving\heart_qr_code.png')

