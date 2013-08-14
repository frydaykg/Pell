import math
from common import *

def getFractionsByRow(a):
	p=[1,a[0]]
	q=[0,1]
	yield (p[1],q[1])
	
	for i in range(1,len(a)):
		p.append(a[i]*p[-1]+p[-2])
		q.append(a[i]*q[-1]+q[-2])
		yield (p[-1],q[-1])


#For n=61
n=61
a=[7, 1, 4, 3, 1, 2, 2, 1, 3, 4, 1, 14, 1, 4, 3, 1, 2, 2, 1, 3, 4, 1, 14, 1, 4, 3, 1, 2, 2, 1, 3, 4, 1, 14]

for (p,q) in getFractionsByRow(a):
	if checkPellSolution(p,q,n):
		print 'Solution for n= %d: x= %d, y=%d' % (n,xx,yy)
		break
