def nod(a,b):
    while a!=0 and b!=0:
        if a>b:
            a = a % b
        else:
            b = b % a
    return a+b

def nok(a,b):
    return a * b / nod(a,b)

def getIntegerFraction(val):
    p=val
    q=1
    while int(p) != p:
        p *=10
        q *=10
    return (int(p),q)

def minus(a,b):
    q = nok(a[1], b[1])
    p1 = a[0] * q / a[1]
    p2 = b[0] * q / b[1]
    p = p1 - p2
    fracNod = nod(p, q)
    return (p / fracNod, q / fracNod)
    

def getContinuedFractionI(val, l = 25):
	a = ( int(val), 1)
	x = minus( getIntegerFraction(val), a)
	l -= 1
	yield int(a[0] / a[1])

	while x[0] != 0 or l > 0:
		a = ( int(x[1] / x[0]), 1)
		x = minus( (x[1], x[0]), a) #1/x - a
		print a,x
		l -= 1
		yield int(a[0] / a[1])

import math
for i in getContinuedFractionI(math.sqrt(2)):
    print i
