import oneColorsStage2 as oC2
def Calc(c, x, d, n, a, b, state):
	temp = 0
	if state == 1:
		temp=abs(oC2.doIt(c[0], b[n-1], d, n, a)-oC2.doIt(c[1], b[n-1], d, n, a))
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
		temp=4*d-abs(oC2.doIt(prim,b[n-1],d,n,a)-oC2.doIt(second,b[n-1],d,n,a))
	if state == 3:
		secondary=['C','M','Y']
		secondary.remove(c[0])
		secondary.remove(c[1])
		temp=max(oC2.doIt(secondary[0],b[n-1],d,n,a), oC2.doIt(secondary[0],a[n-1],d,n,a))
	return temp






def doIt(c, x, d, n, a, b, prims, seconds):
	numtoMake=0
	if prims==2:
		numtoMake=Calc(c, x, d, n, a, b, 1)
	if prims==1:
		numtoMake=Calc(c, x, d, n , a, b, 2)
	if prims==0:
		numtoMake=Calc(c, x, d, n, a, b, 3)
	while numtoMake>364 or numtoMake<-364:
		if numtoMake>364:
			numtoMake=numtoMake-365
		else:
			numtoMake=numtoMake+365
	return numtoMake

