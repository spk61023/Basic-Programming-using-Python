import numpy
#10/6/19 session day4

def fun(r):
    """ Returns area & perimeter of circle given radius r """
    p="n"
    return r, p


def sm():
    return 1,2

x=sm()
print(type(x),x[0],x[1])
a,b=x
print(a,b)
a,b=sm()


print(round(2.484,2))
print(range(10))
print(range(1,10))
print(range(1,10,2))

def wc(greet, name="world"): #only 2nd arg can be supplied having default arguments not for 1st parameter
    print(greet,name)

wc("p1","p2")
wc("p1")
wc(name="p1",greet="p2")
#wc(name="p1","hi")  #positional argument follows keyword argument 

def change():
    global q
    q=10
    print(q)

change()
print(q)


#Mutable variables
name=['Mr.','Steve','Gosling']
def c_n():
    name[0]='Dr.'


c_n()
print(name)

def cn(x):
    x[0]=[1,2,3]
    print(x,'in change')

cn(name)
print(x)

def what(n):
    i=1
    while i*i<n:
        i+=1
    return i*i==n,i

print(what(10))

def whaat(x,n):
        if n<0:
                n=-n
                x=1.0/x
        z=1.0
        while n>0:
            if n%2 == 1:
                z*=x
            x*=x
            n//=2
        return z

print(whaat(2,9))




def hello(x):
    #n=input("enter name")
    #print("Hello ",x)
    return("Hello "+x)
    
x=hello('sam')
print(x)

def adding(x,y):
    #n=input("enter name")
    #print("Hello ",x)
    return(x+y)
    
x=adding(1,2)
print(x)

def is_even(x):
    return x%2==0,x*x           #return multiple values
        
    
x=hello('sam')
print(x)
print(is_even(2)) #even or odd and its square

def greet(name,msg="Hello "):
    return msg+ '' +name

print(greet('sam'))

def to_lower(x):
    res=[]
    for y in x:
            res.append(y.lower())
    return res

print(to_lower(['I','am','BATMAN']))

def fib(n=8):
    a,b=0,1
    res=[0]
    for i in range(n-1):
        res.append(b)
        a,b=b,a+b
    return res
print(fib())

def power2(n=2):
    def f(x):
        return 2**x
    return f

print(power2()(4))

def double(x):
    return 2*x
    
def apply(double,data):
    res=[]
    for x in data:
        res.append(double(x))
    return res
    
print(apply(double,[1,2,3]))

f=open('pendulum.txt')
print(f)
pend=f.read()
print(pend,type(pend))
pend_list = pend.splitlines()
print(pend_list)
f.close()
print(f)


#Reading line by line

for line in open('n1.txt'):
    print(line)

f=open('n1.txt','w')
f.write('hey \n')
print('hi ',file=f)
f.close()

#tokenization
line=" s               p              a ce"
print(line.split())

r="A;010001;ABINESH T N;053;036;28;16;44;177;;;"
print(r.split(';'))
print(r.strip())


#files
f=open('pendulum.txt')
out=open('col2.txt','w')
for line in f:
    fields=line.split()
    print(fields[1],file=out)
f.close()
out.close()
































