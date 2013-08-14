def checkPellSolution(x,y,n):
	return x*x - n*y*y == 1
	
	
def getContinuedFraction(val):
	a = int(val)
	x = val - a
	yield a
	
	while x != 0:
		a = int(1/x)
		x = 1/x - a
		yield a
