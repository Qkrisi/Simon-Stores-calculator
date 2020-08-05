import oneColorsStage3 as oC3
def Calc(c, x, d, n, a, b, cl, state):
	temp = 0
	if state == 1:
		primary=['C','M','Y']
		primary.remove(c[0])
		primary.remove(c[1])
		temp=oC3.doIt(primary[0], cl[n-1], d, n, a, b)+oC3.doIt(primary[0], b[n-1], d, n, a, b)+oC3.doIt(primary[0], a[n-1], d, n, a, b)
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
		temp=min(oC3.doIt(prim, cl[n-1], d, n, a, b), oC3.doIt(second, cl[n-1], d, n, a, b), -(abs(oC3.doIt(prim, cl[n-1], d, n, a, b)-oC3.doIt(second, cl[n-1], d, n, a, b))))
	if state == 3:
		secondary=['C','M','Y']
		secondary.remove(c[0])
		secondary.remove(c[1])
		temp=oC3.doIt(secondary[0], cl[n-1], d, n, a, b)-oC3.doIt(c[0], cl[n-1], d, n, a, b)-oC3.doIt(c[1], cl[n-1], d, n, a, b)
	return temp


def doIt(c, x, d, n, a, b, cl, prims, seconds):
	numtoMake=0
	if prims==2:
		numtoMake=Calc(c, x, d, n, a, b, cl, 1)
	if prims==1:
		numtoMake=Calc(c, x, d, n , a, b, cl, 2)
	if prims==0:
		numtoMake=Calc(c, x, d, n, a, b, cl, 3)
	while numtoMake>364 or numtoMake<-364:
		if numtoMake>364:
			numtoMake=numtoMake-365
		else:
			numtoMake=numtoMake+365
	return numtoMake


