
import fitz,os
doc = fitz.open('F:\\tools\\毛泽东选集1-5\\毛泽东选集5.pdf')
imgcount=0
for page in doc:
    imageList = page.getImageList()
    for imginfo in imageList:
        rect = fitz.Rect(0, 0, 80, 80)
        page.insertImage(rect, filename="test.png", _imgname=imginfo[7])

doc.save('111.pdf')