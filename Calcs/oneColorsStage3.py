def calc(c, x, d, n, a, b):
	temp = 0
	if c=='R':
		temp = x+b[n-1]-a[n-1]
	if c=='G':
		temp = x-2*b[n-1]
	if c=='B':
		temp = x+b[0]-a[3]
	if c=='C':
		temp = x-b[n-1]+a[n-1]
	if c=='M':
		temp = x-2*a[n-1]
	if c=='Y':
		temp = x+b[4]-a[0]
	return temp
	

def doIt(c, x, d, n, a, b):
	numtoMake=calc(c, x, d, n, a, b)
	while numtoMake>364 or numtoMake<-364:
		if numtoMake>364:
			numtoMake=numtoMake-365
		else:
			numtoMake=numtoMake+365
	return numtoMake	

