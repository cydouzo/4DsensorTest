import PIL.Image as im
import math as ma
import pathlib as pa

length = 512

# 1 mm = 3.779527559055 pixels
mm = 3.779527559055;


def gen1D (length):
    source = im.new('L',(length,length),0)
    
    for i in range (0,length):
        if ((i/mm) % 2 < 1):
            for j in range (0,length):
                source.putpixel((i,j),255)
    return source;
    
def gen2D (length):
    source = im.new('L',(length,length),0)
    
    for i in range (0,length):
        for j in range (0,length):
            vali = ((i/mm) % 2) * ma.pi
            valj = ((j/mm) % 2) * ma.pi
            val = int(256*( (1+ma.cos(vali))/2 * (1+ma.cos(valj))/2 ))
            source.putpixel( (i,j) ,  val )
    return source;
    
    
##Question 1.1

source = gen1D(length)
source.show()

##Question 1.2

source = gen2D(length)
source.show()

