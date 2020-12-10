'''
Resizes all images in current working directory to fit
in a 300x300 square,and  adds catlogo.png to the 
lower-right corner
'''

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = '.\py814\ch17\catlogo.png'
logeIm = Image.open(LOGO_FILENAME)
logeWidth,logoHeight=logeIm.size

os.makedirs('.\py814\ch17\withlogo',exist_ok=True)
#TODO:Loop over all files in the working directory.
for filename in os.listdir('.\py814\ch17'):
    if not (filename.endswith('.png') or filename.endswith(',jpg')) \
        or filename == LOGO_FILENAME:
        continue             #skip not-image files and the logo file itself.
    filename1 = '.\py814\ch17\\'+filename
    im = Image.open(filename1)
    width,height = im.size

#TODO:Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:

#TODO:Calculate the new width and height to resize to.
        if width >height:
            height = int((SQUARE_FIT_SIZE/width)*height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE/height)*width)
            height=SQUARE_FIT_SIZE

#TODO:Resize the image.
        print('Resizing %s...' % (filename1))
        im = im.resize((width,height))

#TODO:Add the logo
        print('Adding logo to %s...' % (filename1))
        im.paste(logeIm,(width-logeWidth,height-logoHeight),logeIm)

#TODO:save change.
        im.save(os.path.join('.','py814','ch17','withlogo',filename))