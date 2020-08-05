import oneColorsStage1 as oC1
def Calc(c, x, d, n, a, state):
	temp = 0
	if state == 1:
		temp=max(oC1.doIt(c[0], a[n-1], d, n), oC1.doIt(c[1], a[n-1], d, n))
	if state == 2:
		primary=['R','G','B']
		secondary=['C','M','Y']
		prim = ''
		second = ''
		if c[0] in primary:
			prim=c[0]
			second=c[1]
		else:
			prim=c[1]
			second=c[0]
		temp=oC1.doIt(prim, a[n-1], d, n)+oC1.doIt(second, a[n-1], d, n)-2*d
	if state == 3:
		temp=min(oC1.doIt(c[0], a[n-1], d, n), oC1.doIt(c[1], a[n-1], d, n))
	return temp






def doIt(c, x, d, n, a, prims, seconds):
	numtoMake=0
	if prims==2:
		numtoMake=Calc(c, x, d, n, a, 1)
	if prims==1:
		numtoMake=Calc(c, x, d, n , a, 2)
	if prims==0:
		numtoMake=Calc(c, x, d, n, a, 3)
	while numtoMake>364 or numtoMake<-364:
		if numtoMake>364:
			numtoMake=numtoMake-365
		else:
			numtoMake=numtoMake+365
	return numtoMake
