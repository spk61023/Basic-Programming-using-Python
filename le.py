from pylab import *
L=[.2,.3,.4,.5,.6,.7,.8]
t=[.9,1.19,1.30,1.47,1.58,1.77,1.83]
print(len(L),len(t))
tsq=[]
for time in t:
    tsq.append(time*time) #4spaces Required

plot(L,tsq,'*')
show()