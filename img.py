from pylab import *
clf()
a=imread('lena.png')
imshow(a)
print(a.shape,a.dtype)
rank(a)
b=a[200:400,100:350]
print(b.shape)
imshow(b)
clf()

b=a[::2,::2]
print(b.shape)
imshow(b)
show()