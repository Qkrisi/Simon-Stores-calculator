def calc(c, x, d, n):
	temp = 0
	if c=='R':
		temp = x+d
	if c=='G':
		temp = x-d
	if c=='B':
		temp = 2*x-d
	if c=='C':
		temp = d-x-8*n
	if c=='M':
		temp = 3*n**3-2*x
	if c=='Y':
		temp = x+d-6*n
	return temp
	

def doIt(c, x, d, n):
	numtoMake=calc(c, x, d, n)
	while numtoMake>364 or numtoMake<-364:
		if numtoMake>364:
			numtoMake=numtoMake-365
		else:
			numtoMake=numtoMake+365
	return numtoMake	
