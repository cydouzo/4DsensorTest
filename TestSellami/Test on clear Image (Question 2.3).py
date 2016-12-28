import PIL.Image as im
from Programs import *


source = im.open('lena.bmp')
source.show()

noiseRem1 (source)
source.show()

source = im.open('lena.bmp')
noiseRem2 (source)
source.show()