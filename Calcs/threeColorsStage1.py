import oneColorsStage1 as oC1
def Calc(c, x, d, n, a, state):
	temp=0
	if state==1:
		temp=a[n-1]+a[0]
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
		temp=max(oC1.doIt(prims[0], a[n-1], d, n), oC1.doIt(prims[1], a[n-1], d, n), oC1.doIt(second, a[n-1], d, n))
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
		temp=min(oC1.doIt(seconds[0], a[n-1], d, n), oC1.doIt(seconds[1], a[n-1], d, n), oC1.doIt(prim, a[n-1], d, n))
	if state==4:
		temp=a[n-1]-a[0]
	return temp
	
def doIt(c, x, d, n, a, prims, seconds):
	nomtoMake=0
	if prims==3:
		numtoMake=Calc(c, x, d, n, a, 1)
	if prims==2:
		numtoMake=Calc(c, x, d, n , a, 2)
	if prims==1:
		numtoMake=Calc(c, x, d, n, a, 3)
	if prims==0:
		numtoMake=Calc(c, x, d, n, a, 4)
	while numtoMake>364 or numtoMake<-364:
		if numtoMake>364:
			numtoMake=numtoMake-365
		else:
			numtoMake=numtoMake+365
	return numtoMake

