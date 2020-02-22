from PIL import Image

infile = '/Users/pershing9909/PycharmProjects/coreNet_stuff/2020pro/1582373272403.gif'
outfile = '/Users/pershing9909/PycharmProjects/coreNet_stuff/2020pro/adjust_img.gif'
im = Image.open(infile)
(x,y) = im.size #read image size
x_s = 125 #define standard width
y_s = int(y * x_s / x)#calc height based on standard width
out = im.resize((x_s,y_s),Image.ANTIALIAS) #resize image with high-quality
out.save(outfile)

print('original size: ',x,y)
print('adjust size: ',x_s,y_s)

'''
OUTPUT:
original size:  500 358
adjust size:  250 179
'''