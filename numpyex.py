from numpy import *
from pylab import *
x=linspace(0,1)
import numpy
x=numpy.linspace(0,1)
#plot(x,sin(x))
show()
#numpy arrays
a=array([.1,2,3,4])
b=array([2,3,4,5])
print(a[0],a[-1])
print(a+b,a*b,a/b)
print("--------------------------")
x=linspace(0.0,10.0,200)
x*=2*pi/10
#apply funcions to array
y=sin(x)
y=cos(x)
x[0]=-1
print(x[0],x[-1])

x=array([1.,2,3,4])
print(size(x))
print(x.dtype)
print(x.shape)
print(rank(x))
print(x.itemsize)
print("--------------------------")

a=array([[0,1,2,3],[10,11,12,13]])
print(a.shape)
print(a[1,3])
a[1,3]=-1
print(a[1])

print("--------------------------")
a=array([[0,1,2,3],[10,11,12],[14,15,16]])

print("--------------------------")
a=array([0,1,2,3],dtype=float)
print(ones_like(a))
#print(ones(2,3))
#print(ones_like(a))
print("--------------------------")
x=loadtxt('pendulum.txt')
print(x.shape)
x,y=loadtxt('pendulum.txt',unpack=True)
print(x.shape)
plot(x,y*y,'*')

show()
#x=loadtxt('pendulum.txt')
#L,t=x[:,0]

a=imread('x.png')
imshow(a)

x=4.5

y=2

print(x//y)
import numpy as np
a=np.array([[1,2,3],[0,1,4]])
b=np.zeros((2,3))
c=np.ones((2,3))
d=a+b+c
print(d[1,2])

x=True
y=False
z=False
if x or y and z:
    print("yes")
else:
    print("no")

list1=[1,2,3,4]
list2=[5,6,7,8]
print(len(list1+list2))
a=np.array([[0,1,0],[1,0,1]])
a+=3
b=a+3
print(a[1,2]+b[1,2])



















