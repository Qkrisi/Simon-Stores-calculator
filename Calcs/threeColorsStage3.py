import oneColorsStage3 as oC3
def Calc(c, x, d, n, a, b, cl, state):
	temp=0
	if state==1:
		temp=cl[n-1]+(cl[n-1]%3)*cl[0]-(b[n-1]%3)*b[0]+(a[n-1]%3)*a[0]
	if state==2:
		primary=['R','G','B']
		secondary=['C','M','Y']
		prims=[]
		second = ''
		for i in range(3):
			if c[i] in primary:
				prims.append(c[i])
			else:
				second=c[i]
		temp=oC3.doIt(prims[0], cl[n-1], d, n, a, b)+oC3.doIt(prims[1], cl[n-1], d, n, a, b)-oC3.doIt(second, b[n-1], d, n, a, b)-oC3.doIt(second, a[n-1], d, n, a, b)
	if state==3:
		primary=['R','G','B']
		secondary=['C','M','Y']
		prim=''
		seconds = []
		for i in range(3):
			if c[i] in secondary:
				seconds.append(c[i])
			else:
				prim=c[i]
		temp=oC3.doIt(seconds[0], cl[n-1], d, n, a, b)+oC3.doIt(seconds[1], cl[n-1], d, n, a, b)-oC3.doIt(prim, b[n-1], d, n, a, b)-oC3.doIt(prim, a[n-1], d, n, a, b)
	if state==4:
		temp=cl[n-1]+(cl[0]%3)*cl[n-1]-(b[0]%3)*b[n-1]+(a[0]%3)*a[n-1]
	return temp
	
def doIt(c, x, d, n, a, b, cl, prims, seconds):
	nomtoMake=0
	if prims==3:
		numtoMake=Calc(c, x, d, n, a, b, cl, 1)
	if prims==2:
		numtoMake=Calc(c, x, d, n , a, b, cl, 2)
	if prims==1:
		numtoMake=Calc(c, x, d, n, a, b, cl, 3)
	if prims==0:
		numtoMake=Calc(c, x, d, n, a, b, cl, 4)
	while numtoMake>364 or numtoMake<-364:
		if numtoMake>364:
			numtoMake=numtoMake-365
		else:
			numtoMake=numtoMake+365
	return numtoMake



