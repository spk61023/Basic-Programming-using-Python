import numpy
def f(x): return x+2
def safe_run(f,x):
   try:
       f(x)
   except ValueError:
        return 'ValueError'
   except TypeError:
        return 'TypeError'
   else:
        return 'OK' 
            

print(safe_run(f,'2'))
print(safe_run(float,'A'))
