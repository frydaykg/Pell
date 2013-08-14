def checkPellSolution(x,y,n):
	if x*x-n*y*y==1:
		return True
	return False
	
	
def getContinuedFraction(val):
	a=[int(val)]
	x=[val-a[0]]
	yield a[0]
	
	while True:
		a.append(int(1/x[-1]))
		xx.append(1/x[-1]-a[-1])
		yield a[-1]

