def calc(c, x, d, n, a):
	temp = 0
	if c=='R':
		temp = x+a[n-1]+n**2
	if c=='G':
		temp = 2*x-a[n-1]
	if c=='B':
		temp = 2*x-a[0]-4*n**2
	if c=='C':
		temp = x+a[1]
	if c=='M':
		temp = x+a[2]-d
	if c=='Y':
		temp = x+a[3]-a[n-1]
	return temp
	

def doIt(c, x, d, n, a):
	numtoMake=calc(c, x, d, n, a)
	while numtoMake>364 or numtoMake<-364:
		if numtoMake>364:
			numtoMake=numtoMake-365
		else:
			numtoMake=numtoMake+365
	return numtoMake	
