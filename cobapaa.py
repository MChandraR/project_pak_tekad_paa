from PIL import Image, ImageDraw
import random

size = 50
canvas = Image.new("RGB",(1000,1000), "green" )

bangunan = Image.open("image/buildings.png")

canvas.paste(bangunan, (0,0) )
 
imageEdit = ImageDraw.Draw(canvas)
#blablbalblabl

for i in range(10):
    if not random.randint(0,2):
        imageEdit.rectangle(xy = (i*100, 0 , i*100+20,1000 ), fill = (0,0,0))
    if not random.randint(0,2):
        imageEdit.rectangle(xy = (0, i*100 , 1000,i*100+20 ), fill = (0,0,0))
    
canvas.show()


