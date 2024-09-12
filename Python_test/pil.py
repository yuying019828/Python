from PIL import Image
import os

im=Image.open('picture.png')

#???
gray=im.convert('L')
gray.show()

#??
box=(100,100,400,400)
region=im.crop(box)
region.show()

#????
region=region.transpose(Image.ROTATE_180)
region.show()
im.paste(region,box)
im.show()

#???????
out=im.resize((200,200))
out=out.rotate(45)
out.show()

im.thumbnail((100,100))
im.show()


