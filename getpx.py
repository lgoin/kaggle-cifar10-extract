import PIL as Pillow
from PIL import Image
import sys
import os

labels = []
f = open("beetrainLabels.csv")
for line in f:
	labels.append( '"' + line.rstrip().split(',')[1] + '"' )
f.close()

arr = []
for i in range(0,200*200):
	for j in ['r','g','b']:
		arr.append('"px' + j + str(i) + '"')
arr.append('"class"')
print ",".join(arr)



for x in range(1, 50000+1):
        if os.path.isfile('beetrain/' + str(x) + '.jpg'):
        
                #im = Image.open('beetrain/' + str(x) + '.jpg').convert('LA')
                im = Image.open('beetrain/' + str(x) + '.jpg')

                #im.show()
                
                arr = []
                for i in range(0, 200):
                        for j in range(0, 200):
                                tp = im.getpixel((i,j))
                                arr.append( str(tp[0]) )
                                arr.append( str(tp[1]) )
                                arr.append( str(tp[2]) )
                                
                print ",".join(arr) + "," + labels[x]

	else:
                pass
