#What this script does:
#takes the image file in the same folder like this script lies and resamples it to a specific number of pixels
#draws some white boxes to delete text, which was already visible in the original image
#adds your newly defined text to the image and saves it

#to do: you have to download a .ttf file (fonts) first, e.g. arial and specify the location of this .fft file further below
#copy your image file you want to edit and this script into the same folder - note there should be only one such image file in the folder - and run it

import os, sys
import PIL
from PIL import Image, ImageFont, ImageDraw


#Set the file path, filepath is where the .py file is
files_path = os.getcwd()
files_path = os.path.join(files_path, '') #Adds the \\ to the end of the path name

lst = os.listdir(files_path)


#select the image
for file_name in lst:
    if file_name.endswith(".png"):
       imagefile = file_name   
 
# resize the image so they are always the same size
img = Image.open(imagefile)
img.thumbnail(size=(2121,1500))
img.save(imagefile, optimize=True)


img2 = Image.open(imagefile)

#define text font, also defines font size

ttffile = 'D:\\fonts\\arial.ttf'

# you can change the text size here       
text_font = ImageFont.truetype(ttffile, 20)
text_font2 = ImageFont.truetype(ttffile, 40)

#type in the text
text_1 = raw_input('Enter your desired text for field 1.    e.g. This is an example: ')

print "Enter/Paste your content. Ctrl-Z + Enter to save it."

text_2 = []
while True:
    try:
        line = raw_input("Enter your desired text for field 2: ")
    except EOFError:
        break
    text_2.append(line)
text_2="\n".join(text_2)


text_3 = [] 
while True:
    try:
        line = raw_input('Enter your desired text for field 3: ')
    except EOFError:
        break
    text_3.append(line)
text_3="\n".join(text_3)



#draw white boxes - you can change the location and size by adjusting the coordinates
d = ImageDraw.Draw(img2)
d.rectangle([(40, 75), (350, 175)], outline=None, fill=(255, 255, 255), width=1)
d.rectangle([(360, 75), (1140, 213)], outline=None, fill=(255, 255, 255), width=1)
d.rectangle([(1147, 75), (1900, 213)], outline=None, fill=(255, 255, 255), width=1)

#write the text to the image, define start coordinates and color
d.text((45,100), text_1, (255, 10, 10), font=text_font2)
d.multiline_text((370,80), text_2, (10, 10, 10), font=text_font)
d.multiline_text((1160,80), text_3, (10, 10, 10), font=text_font)

#rename the file
img2.save('result'+imagefile[11:])


 
raw_input('DONE ----- Press ENTER to exit')
