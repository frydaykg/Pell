def checkPellSolution(x,y,n):
	return x*x - n*y*y == 1
	
	
def getContinuedFraction(val):
	a = [ int(val) ]
	x = [ val - a[0] ]
	yield a[0]
	
	while True:
		a.append(int(1/x[-1]))
		xx.append(1/x[-1]-a[-1])
		yield a[-1]

