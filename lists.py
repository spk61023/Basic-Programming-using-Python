from pylab import *
mlist=[]
p=[2,3,5,7]
print(p[1])
print(p[0]+p[1]+p[-1])
print(p[-1])
print(p[-2])
#slice operation
print('slice Operation : ',p[1:3],p[0:-1],p[0:])
print(p[0:4:2]) #::2
print(p[1:-1:2])

b=[11,13,17]
c=p+b
print(c)
p.append(11)
print(p)