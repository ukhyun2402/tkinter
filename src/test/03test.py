from PIL import Image, ImageDraw

img = Image.open('./img/jail.png').convert("RGB")
h,w = img.size

alpha = Image.new('L', img.size,0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([0,0,h,w],0,360,fill=255)