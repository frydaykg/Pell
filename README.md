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

a_0 = int(x)              
x_0 = x - a_0


a_1 = int(1 / x_0)        
x_1 = 1 / x_0 - a_1


a_n = int(1 / x_[n-1])    
x_n = 1 / x_[n-1] - a_n


Calculation of convergent fractons by continued fraction

p_[-1] = 1       
q_[-1] = 0         


p_0 = a_0      
q_0 = 1


p_n = a_n * p_[n-1] + p_[n-2]       
q_n = a_n * q_[n-1] + q_[n-2]
