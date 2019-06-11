from pylab import *
a=13 #int

b=9999999999999999999999999999999999999 #anysize

p=3.141 #float

c=3+4j #complex

print(a,b,p,c)

#Booleans   
b=True
a=False
c=True
print(a and b or c)
print(a and (b or c))
print(a and b or c)
#( ) for precedence
print('string')
print("string")
print("""string """)
print('''string''')
w="hello"
print(w[0],w[-1])
print(len(w))
#strings are immutable
#finding data type

print(type(w))

#operators
a=1786%12
b=3*3
c=123456789123456789 ** 3
vb=c * c * c * c * c * c * c *c *c
X=17/2  #anything is float
Y=17 // 2 #floor division
Z=17 // 2.0
A=3+4j
print(A.imag)
print(A.real)
print(A.conjugate)
print('abs(A) =',abs(A))
print(a,b,c,vb,X,Y,Z)
a=7456
a+=1
print(a)
a-=1
print(a)

s='the'
p='sam19'
print("string",s+p)
print("string",s*4)


print(s.startswith(s))
print(s.endswith('m'))
print('Upper case',s.upper(),'lowercase',s.lower())

s1=s.strip()
print("strip ",s1)
print("string index",s1.index('t'))
print('replace',s1.replace('the','I am'))
print("string",s1)

chars ='a b c'
print(chars.split())
print('#'.join(['a','b','c']))
a='#'.join(['a','b','c'])
print(a.split)

name=input()           #input
print("Hello",name)

#promt the :>Please enter your name: 
n=input("Please enter your name: ")
print("Hello",n)

x=int(input("Enter a No.  "))
y=str(x*x)

print("Square= ",len(y)) #Digits of integer

x=input()
x=int(x)
print(x%2!=0)

n=input()
print(n.upper())

f=input()
print(f+'.txt')


#str functions
st=input()
print(st[1:])
print()
print(st[::1])



m=input()
m=m.lower()
n=(m.count('a'))












