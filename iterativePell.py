import math
from common import *


#iterative solution for n in range 1 to 1000
for D in xrange(1,1001):
	if int(math.sqrt(D))**2==D:
		print 'No solution for n= %d'% D
		continue
	
	#init	
	sq=math.sqrt(D)
	
	a=[math.floor(sq)]
	x=[sq-a[0]]
	a.append(math.floor(1/x[0]))
	x.append(1/x[0]-a[1])
	
	p=[a[0],a[1]*a[0]+1]
	q=[1,a[1]]
	
	while True:
		xx=p[-1]
		yy=q[-1]
		if checkPellSolution(xx,yy,D):
			print 'Solution for n= %d: x= %d, y=%d' % (D,xx,yy)
			break
		#calculate next values
		a.append(math.floor(1/x[-1]))
		x.append(1/x[-1]-a[-1])
		p.append(a[-1]*p[-1]+p[-2])
		q.append(a[-1]*q[-1]+q[-2])
