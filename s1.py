from PIL import Image
from pylab import *

img = array(Image.open('../images/house.png'))
imshow(img)

x=[100,100,400,400]
y=[200,500,200,500]

plot(x,y,'ks-')

plot(x[:2],y[:2])

title('Plotting : "house.png"')
show()
