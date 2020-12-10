from PIL import Image

catIm=Image.open('.\py814\ch17\zophie.png')
faceIm=Image.open('.\py814\ch17\cp.png')
catImWight,catImHeight=catIm.size
faceImWeight,faceImHeight=faceIm.size
catcpTwo=catIm.copy()
for left in range(0,catImWight,faceImWeight):
    for top in range(0,catImHeight,faceImHeight):
        print(left,top)
        catcpTwo.paste(faceIm,(left,top))
catcpTwo.save('py814\ch17\\title.png')