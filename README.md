# Basic-Programming-using-Python
Basic-Programming-using-Python - It Contains the files related to the Workshop done using Python 3 . If you are executing the same please install Canopy and version 3.X is preferred! 

The Documentation of Files

Python Workshop

Django for web based apps
-Python std libarary
-interpretor
-Distribution

Starting terminal ipthon
$ ipython --pylab

In [1]: IPython prompt

Exiting on the terminal  In[ ]:^D 

IPython : enhanced interpretor 


Breaking out of loops
^C

4spaces / indentation
continuation prompt ...:

Plotting
x = linspace(0, 2*pi, 50)
plot(x,sin(x))

-> linspace(start,stop,num)

Decoration
xlabel('')
ylabel('')

clf() to clear

more decoration
title('')
legend([''],loc='')
center,right,left,best

# --> comment

plot(,,'r')

annotate('text',xy=(x,y))



pl<TAB> to autocomplete


Overlaid Plots
y=linspace(0,2*pi,50)

In [33]: clf()

In [34]: plot(y,sin(y))
Out[34]: [<matplotlib.lines.Line2D at 0x22cacbf56a0>]

In [35]: plot(y,cos(y))
Out[35]: [<matplotlib.lines.Line2D at 0x22cacc28198>]

In [36]: xlabel('y')
Out[36]: <matplotlib.text.Text at 0x22cacbbe080>

In [37]: ylabel('f(y)')
Out[37]: <matplotlib.text.Text at 0x22cacbbfeb8>

In [38]: legend(['sin(y)','cos(y)'])
Out[38]: <matplotlib.legend.Legend at 0x22cacc18668>

plotting seperate fig
clf()

In [40]: figure(1)
Out[40]: <matplotlib.figure.Figure at 0x22cacbb57b8>

In [41]: plot(y,sin(y))
Out[41]: [<matplotlib.lines.Line2D at 0x22cacc8c2e8>]

In [42]: figure(2)
Out[42]: <matplotlib.figure.Figure at 0x22cacc04c50>

In [43]: plot(y,cos(y))
Out[43]: [<matplotlib.lines.Line2D at 0x22caccfb198>]

In [44]: savefig('cosine.png')

In [45]: figure(1)
Out[45]: <matplotlib.figure.Figure at 0x22cacbb57b8>

In [46]: title('Sin(y)')
Out[46]: <matplotlib.text.Text at 0x22cacc6ae80>

In [47]: savefig('sine.png')

In [48]: close()

In [49]: close()


Get Axex Lengths
xmin, xmax = xlim()

In [51]: ymin,ymax=ylim()

In [52]: print(xmin,xmax)
0.0 1.0

Set the axes limits
In [53]: xlim(xmin,2*pi)
Out[53]: (0.0, 6.283185307179586)

In [54]: ylim(ymin-0.2, ymax+0.2)
Out[54]: (-0.20000000000000001, 1.2)

Documentation

plot?

For Function use : plot??

----------------------------------------------------
session 2
%hist  - cmd history
%save script_name line_no's

%hist -n : to know line no.
%pwd : Present Working Directory
%cd : Change Dir
%run scriptname.py
%run -i script.py
show()

to import

from pylab import linspace

from pylab import *

saving files : naming conventions
------------------------------------------------

CANOPY
Ctrl R
Ctrl + Shift S
-----------------------------------------------
session 3

plotting

lists
list [initial:final:step]
mlist=[]
p=[2,3,5,7]
print('slice Operation : ',p[1:3],p[0:-1],p[0:])
+, append
----------------------------------------------
simple pendulum /numpy

%time
%timeit
size,shape,rank
striding
-------------------------------------------------
elementary image processing
a=imread('lena.png')
imshow(a)
--------------------------------------------------
Day 2

session 1

Image cropping
resizing,slcing,striding
data types - No's, Boolean, strings

Operators
-----------------------------------
ctrl shift R
--------------------------------------
def fun(r):
""" Returns area & perimeter of circle given radius r """
return r,p


built in functions
abs,any,lenth,all etc


For visulaization of the code at each step view the website pythontutor.com


finally
final
finalize
