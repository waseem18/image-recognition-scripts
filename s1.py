from PIL import Image
from pylab import *

img = array(Image.open('../images/house.png').convert('L'))

show()
