from PIL import Image, ImageFilter

im = Image.open('Lenna.png')
print "The size of the image is: "
print (im.format, im.size, im.mode)

blurred = im.filter(ImageFilter.BLUR)

im.show()
blurred.show()
im = im.filter(ImageFilter.CONTOUR)

im.save("lenna" + ".jpg")
im.show()

blurred.save("blurredLenna.png")
