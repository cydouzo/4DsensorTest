import PIL.Image as im
import math as ma
import pathlib as pa

# 1 mm = 3.779527559055 pixels
mm = 3.779527559055;

        
def noiseRem1 (source):
    (width,length) = source.size
    for i in range (1,width-1):
        for j in range (1,length-1):
            average = ( source.getpixel((i,j+1)) + source.getpixel((i,j-1)) + source.getpixel((i+1,j)) + source.getpixel((i-1,j)) )//4
            if abs( average - source.getpixel((i,j)) ) > 10:
                source.putpixel((i,j),average)
               
def noiseRem2 (source):
    (width,length) = source.size
    for i in range (1,width-1,2):
        for j in range (1,length-1,2):
            average = 0;
            for k in range(-1,2):
                for l in range(-1,2):
                    average += source.getpixel((i+k,j+l)) /9
            if abs( average - source.getpixel((i,j)) ) > 10:
                maxMin = [(0,0),(0,0),(0,0),(0,0)] #This array will contain the extremums as follow: [max1,max2,min1,min2]
                M , m = -1 , 256
                for k in range(-1,2):
                    for l in range(-1,2):
                        if source.getpixel((i+k,j+l)) > M:
                            maxMin[0] = (i+k,j+l)
                            M = source.getpixel((i+k,j+l))
                        if source.getpixel((i+k,j+l)) < m:
                            maxMin[2] = (i+k,j+l)
                            m = source.getpixel((i+k,j+l))
                M , m = -1 , 256
                for k in range(-1,2):
                    for l in range(-1,2):
                        if (i+k,j+l) != maxMin[0] and (i+k,j+l) != maxMin[2] and source.getpixel((i+k,j+l)) > M:
                            maxMin[1] = (i+k,j+l)
                            M = source.getpixel((i+k,j+l))
                        if (i+k,j+l) != maxMin[0] and (i+k,j+l) != maxMin[2] and source.getpixel((i+k,j+l)) <= m:
                            maxMin[3] = (i+k,j+l)
                            m = source.getpixel((i+k,j+l))
                            
                average = 0;
                t=0
                for k in range(-1,2):
                    for l in range(-1,2):
                        if not ((i+k,j+l) in maxMin):
                            average += source.getpixel((i+k,j+l)) /5
                            t+=1
                if (t!=5):
                    print(maxMin)
                average = int(average)
                for m in maxMin:
                    source.putpixel(m,average)

#Question 2.1 and 2.2

source = im.open('lenaNoise.jpg')
source.show()

noiseRem1 (source)
source.show()

source = im.open('lenaNoise.jpg')
noiseRem2 (source)
source.show()
