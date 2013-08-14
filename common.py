def checkPellSolution(x,y,n):
	return x*x - n*y*y == 1
	
	
def getContinuedFraction(val, l = 25):
	a = int(val)
	x = val - a
	l -= 1
	yield a
	
	while x != 0 or l > 0:
		a = int(1/x)
		x = 1/x - a
		l -= 1
		yield a
