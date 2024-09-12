from PIL import Image
from pylab import *
from numpy import array

im = array(Image.open('picture.png'))

imshow(im)
# set the x and y axis limits (100, 200) \ (100, 500) \ (400, 200) \ (400, 500)
x = [100,100,400,400]
y = [200,500,200,500]


plot(x,y,'r*')
plot(x[:2],y[:2])

# set the title of the plot
title('Plotting: "picture.png"')

#axis('off')
show()

# ????
im_gray = Image.open('picture.png').convert('L')  # ??????
im2 = 255 - array(im_gray) 
imshow(im2, cmap='gray')
title('Reverse Image')
show()