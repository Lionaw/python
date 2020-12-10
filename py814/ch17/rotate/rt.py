from PIL import Image

catIm=Image.open('.\py814\ch17\zophie.png')
#catIm.rotate(90).save('.\py814\ch17\\rotate\90.png')
#catIm.rotate(180).save('.\py814\ch17\\rotate\\180.png')
#catIm.rotate(270).save('.\py814\ch17\\rotate\\270.png')
#catIm.rotate(9).save('.\py814\ch17\\rotate\9.png')
#catIm.rotate(9,expand=True).save('.\py814\ch17\\rotate\9e.png')
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('.\py814\ch17\\rotate\FLR.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('.\py814\ch17\\rotate\FTB.png')