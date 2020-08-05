import oneColorsStage2 as oC2
def Calc(c, x, d, n, a, b, state):
	temp=0
	if state==1:
		temp=b[n-1]+(b[n-1]%4)*b[0]-a[3]
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
		temp=b[n-1]+oC2.doIt(prims[0], b[n-1], d, n, a)+oC2.doIt(prims[1], b[n-1], d, n, a)-oC2.doIt(second, a[n-1], d, n, a)
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
		temp=b[n-1]+oC2.doIt(seconds[0], a[n-1], d, n, a)+oC2.doIt(seconds[1], a[n-1], d, n, a)-oC2.doIt(prim, b[n-1], d, n, a)
	if state==4:
		temp=b[n-1]+(b[0]%4)*b[n-1]-a[3]
	return temp
	
def doIt(c, x, d, n, a, b, prims, seconds):
	nomtoMake=0
	if prims==3:
		numtoMake=Calc(c, x, d, n, a, b, 1)
	if prims==2:
		numtoMake=Calc(c, x, d, n , a, b, 2)
	if prims==1:
		numtoMake=Calc(c, x, d, n, a, b, 3)
	if prims==0:
		numtoMake=Calc(c, x, d, n, a, b, 4)
	while numtoMake>364 or numtoMake<-364:
		if numtoMake>364:
			numtoMake=numtoMake-365
		else:
			numtoMake=numtoMake+365
	return numtoMake


