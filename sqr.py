from pylab import *
L=[.2,.3,.4,.5,.6,.7,.8]
t=[.9,1.19,1.30,1.47,1.58,1.77,1.83]
def sqr(x):
    
    return x+2
print(sqr(1))

def su(a,b):
    return a+b

print(su(1,2))

def test():
    print("finished")
    return 
    
print(test())


t=array(t)
tsq=t*t
print(tsq)
plot(L,tsq)

#t=range(1000000)
#tsq=sqr(t)
#print(sqr(t))

#t=array(t)
#tsq=t*t
#print(tsq(t))

s=range(100000)
s=array(s)
len(s)
s=linspace(0,10,10000)
#%timeit s*s

