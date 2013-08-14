Pell
====

Pell's equation solver

Files
=====

pell.py  
Contain solution for n=61. Continued fraction of sufficient length precalculated. Code calculate right convergent fractions and find out solution.

common.py  
Contain function for Pell's equation checking and continued fractions generator.

iterativePell.py   
Try to find solution of Pell's equation for n from 1 to 1000. Code hover on n=61.

pell.cpp   
Check continued fracton generation for n=61. It's already known, that solution achieved on 21 step(in n=61 case). That't why N=30 enough for calculation. Code calculate incorrect continued fraction.


Some math
============

Calculation of continued fraction for x

a[0] = int(x)              
x[0] = x - a[0]


a[1] = int(1 / x[0])        
x[1] = 1 / x[0] - a[1]


a[n] = int(1 / x[n-1])    
x[n] = 1 / x[n-1] - a[n]


Calculation of convergent fractons by continued fraction

p[-1] = 1       
q[-1] = 0         


p[0] = a[0]      
q[0] = 1


p[n] = a[n] * p[n-1] + p[n-2]       
q[n] = a[n] * q[n-1] + q[n-2]
