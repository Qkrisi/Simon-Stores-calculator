import sys
import os
import platform
from itertools import cycle, islice, dropwhile

debugMode = False
debugInput = str(input('Do you want to use debug mode? (Y/N) '))
if(debugInput=='Y' or debugInput=='y'):
	debugMode = True
	
def clearScreen():
	if(not(debugMode)):
		if(platform.system()=='Windows'):
			os.system('cls')
		else:
			os.system('clear')
	else:
		return


clearScreen()
serialNum = str(str(input('Serial number: ')).upper())
colors=str(str(input('Enter colors starting from white going in clockwise! ')).upper())
colors=colors.replace('W','')
colors=colors.replace('K','')
colors=list(map(str, colors.split()))

a=[]
b=[]
c=[]
allcolors=[['R', 'G', 'B', 'C', 'M', 'Y'], ['Y', 'B', 'G', 'M', 'C', 'R'], ['B', 'M', 'R', 'Y', 'G', 'C']]
base36=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
opposites = [[1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3]]



temp = 0
if serialNum[2] in numbers:
	temp=int(serialNum[2])*36
else:
	temp=base36.index(serialNum[2])*36
	
if serialNum[3] in numbers:
	temp+=int(serialNum[3])
else:
	temp+=base36.index(serialNum[3])
while temp>364 or temp<-364:
		if temp>364:
			temp=temp-365
		else:
			temp=temp+365
a.append(temp)
temp=0
if serialNum[4] in numbers:
	temp=int(serialNum[4])*36
else:
	temp=base36.index(serialNum[4])*36
print(temp)
if serialNum[5] in numbers:
	temp+=int(serialNum[5])
else:
	temp+=base36.index(serialNum[5])
while temp>364 or temp<-364:
		if temp>364:
			temp=temp-365
		else:
			temp=temp+365
b.append(temp)
print(b)
temp=0
if serialNum[0] in numbers:
	temp=int(serialNum[0])*36
else:
	temp=base36.index(serialNum[0])*36
if serialNum[1] in numbers:
	temp+=int(serialNum[1])
else:
	temp+=base36.index(serialNum[1])
while temp>364 or temp<-364:
		if temp>364:
			temp=temp-365
		else:
			temp=temp+365
c.append(temp)
ossz=(int(base36.index(serialNum[0])+base36.index(serialNum[1])+base36.index(serialNum[2])+base36.index(serialNum[3])+base36.index(serialNum[4])+base36.index(serialNum[5])))
currentcolors=[]

sys.path.insert(1, './Calcs')
print(a[0],b[0],c[0])
import oneColorsStage1 as oC1
import oneColorsStage2 as oC2
import oneColorsStage3 as oC3
import twoColorsStage1 as tC1
import twoColorsStage2 as tC2
import twoColorsStage3 as tC3
import threeColorsStage1 as thC1
import threeColorsStage2 as thC2
import threeColorsStage3 as thC3
import balancedTernary as Con2Bal
primary=['R','G','B']
secondary=['C','M','Y']

clearScreen()
aColors=list(map(str, str(input('Enter colors for the 1st stage! ')).split()))

def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def doColors(stage):
	currentcolors=allcolors[stage-1]
	print(currentcolors)
	if(colors[0]=='Y'):
		print('true1')
		currentcolorstocycle=cycle(currentcolors)
		skipped = dropwhile(lambda x: x != currentcolors[-1], currentcolorstocycle)
		sliced = islice(skipped, None, 6)
		currentcolors=list(sliced)
		print(currentcolors)
	if(opposites[1][opposites[0][colors.index('R')]-1]==colors.index('C')+1):
		print('true2')
		for i in range(6):
			if(currentcolors[i]=='R'):
				currentcolors[i]='C'
				continue
			if(currentcolors[i]=='C'):
				currentcolors[i]='R'
				continue
			if(currentcolors[i]=='G'):
				currentcolors[i]='M'
				continue
			if(currentcolors[i]=='M'):
				currentcolors[i]='G'
				continue
			if(currentcolors[i]=='B'):
				currentcolors[i]='Y'
				continue
			if(currentcolors[i]=='Y'):
				currentcolors[i]='B'
				continue
		print(currentcolors)
	if(colors.index('G')+1==1 or colors.index('G')+1 == 6):
		print('true3')
		for i in range(6):
			if(currentcolors[i]=='R'):
				currentcolors[i]='G'
				continue
			elif(currentcolors[i]=='G'):
				currentcolors[i]='B'
				continue
			elif(currentcolors[i]=='B'):
				currentcolors[i]='R'
				continue
			else:
				continue
		print(currentcolors)
	if(colors.index('M')+1==3 or colors.index('M')+1 == 4):
		print('true4')
		for i in range(6):
			if(currentcolors[i]=='C'):
				currentcolors[i]='M'
				continue
			elif(currentcolors[i]=='M'):
				currentcolors[i]='Y'
				continue
			elif(currentcolors[i]=='Y'):
				currentcolors[i]='C'
				continue
			else:
				continue
		print(currentcolors)
	if((colors.index('B')+1==1 and (colors.index('Y')+1==2 or colors.index('Y')+1==3)) or (colors.index('B')+1==2 and (colors.index('Y')+1==1 or colors.index('Y')+1==3)) or (colors.index('B')+1==3 and (colors.index('Y')+1==1 or colors.index('Y')+1==2)) or (colors.index('B')+1==4 and (colors.index('Y')+1==5 or colors.index('Y')+1==6)) or (colors.index('B')+1==5 and (colors.index('Y')+1==4 or colors.index('Y')+1==6)) or (colors.index('B')+1==6 and (colors.index('Y')+1==4 or colors.index('Y')+1==5))):
		print('true5')
		currentcolors=swapPositions(currentcolors, currentcolors.index('B'), 5-currentcolors.index('B'))
		print(currentcolors)
	if(colors.index('R')+1==1 or colors.index('R')+1==2 or colors.index('R')+1==3):
		print('true6')
		currentcolors=swapPositions(currentcolors, currentcolors.index('R'), currentcolors.index('Y'))
		print(currentcolors)
	if(colors.index('B')+1==4 or colors.index('B')+1==5 or colors.index('B')+1==6):
		print('true7')
		currentcolors=swapPositions(currentcolors, currentcolors.index('G'), currentcolors.index('C'))
		print(currentcolors)
	return currentcolors

for i in range(3):
	if(len(aColors[i])==1):
		a.append(oC1.doIt(aColors[i], a[i], ossz, i+1))
	if(len(aColors[i])==2):
		prims=0
		seconds=0
		for j in range(2):
			if aColors[i][j] in primary:
				prims+=1
			else:
				seconds+=1
		a.append(tC1.doIt(aColors[i], a[i], ossz, i+1, a, prims, seconds))
	if(len(aColors[i])==3):
		prims=0
		seconds=0
		for j in range(3):
			if aColors[i][j] in primary:
				prims+=1
			else:
				seconds+=1
		a.append(thC1.doIt(aColors[i], a[i], ossz, i+1, a, prims, seconds))
		
a.append(0)
print(ossz)
print(a)

negate = False
if(a[3]!=0):
	if(a[3]<0):
		negate = True
		finallist = Con2Bal.doIt(a[3]*-1)
	else:
		finallist = Con2Bal.doIt(a[3])
	#print(negate)
	if(negate):
		#print(finallist)
		for i in range(6):
			if(finallist[i]==1):
				finallist[i]='Z'
				continue
			if(finallist[i]=='Z'):
				finallist[i]=1
				continue
			if(finallist[i]==0):
				continue
	#print(finallist)
	finalstring = []
	finalcolors=doColors(1)
	fullfinallist=[]
	if(len(finallist)<6):
		for i in range(6-len(finallist)):
			fullfinallist.append(0)
		for i in finallist:
			fullfinallist.append(i)
	else:
		fullfinallist=finallist
	for i in range(6):
		if(fullfinallist[i]==1):
			finalstring.append(f'+{finalcolors[i]}')
			continue
		elif(fullfinallist[i]=='Z'):
			finalstring.append(f'-{finalcolors[i]}')
			continue
		else:
			continue
	print(len(finallist), len(fullfinallist), finallist, fullfinallist, a)
	clearScreen()
	input(''.join(finalstring))
else:
	clearScreen()
	input('The answer is 0!')
clearScreen()
aColors.append(str(input('Enter additional flash for 2nd stage! ')))

for i in range(4):
	if(len(aColors[i])==1):
		b.append(oC2.doIt(aColors[i], b[i], ossz, i+1, a))
	if(len(aColors[i])==2):
		prims=0
		seconds=0
		for j in range(2):
			if aColors[i][j] in primary:
				prims+=1
			else:
				seconds+=1
		b.append(tC2.doIt(aColors[i], b[i], ossz, i+1, a, b, prims, seconds))
	if(len(aColors[i])==3):
		prims=0
		seconds=0
		for j in range(3):
			if aColors[i][j] in primary:
				prims+=1
			else:
				seconds+=1
		b.append(thC2.doIt(aColors[i], b[i], ossz, i+1, a, b, prims, seconds))

negate = False
if(b[4]!=0):
	if(b[4]<0):
		negate = True
		finallist = Con2Bal.doIt(b[4]*-1)
	else:
		print(b[4])
		finallist = Con2Bal.doIt(b[4])
		print(finallist)
	#print(negate)
	if(negate):
		#print(finallist)
		for i in range(6):
			if(finallist[i]==1):
				finallist[i]='Z'
				continue
			if(finallist[i]=='Z'):
				finallist[i]=1
				continue
			if(finallist[i]==0):
				continue
				
	finalstring = []
	finalcolors=doColors(2)
	fullfinallist=[]
	if(len(finallist)<6):
		for i in range(6-len(finallist)):
			fullfinallist.append(0)
		for i in finallist:
			fullfinallist.append(i)
	else:
		fullfinallist=finallist
	print(fullfinallist)
	for i in range(6):
		if(fullfinallist[i]==1):
			finalstring.append(f'+{finalcolors[i]}')
			continue
		elif(fullfinallist[i]=='Z'):
			finalstring.append(f'-{finalcolors[i]}')
			continue
		else:
			continue

	print(b)
	clearScreen()
	input(''.join(finalstring))
else:
	clearScreen()
	input('The answer is 0!')
clearScreen()
aColors.append(str(input('Enter additional flash for 3rd stage! ')))
for i in range(5):
	if(len(aColors[i])==1):
		c.append(oC3.doIt(aColors[i], c[i], ossz, i+1, a, b))
	if(len(aColors[i])==2):
		prims=0
		seconds=0
		for j in range(2):
			if aColors[i][j] in primary:
				prims+=1
			else:
				seconds+=1
		c.append(tC3.doIt(aColors[i], c[i], ossz, i+1, a, b, c, prims, seconds))
	if(len(aColors[i])==3):
		prims=0
		seconds=0
		for j in range(3):
			if aColors[i][j] in primary:
				prims+=1
			else:
				seconds+=1
		c.append(thC3.doIt(aColors[i], c[i], ossz, i+1, a, b, c, prims, seconds))

negate = False
if(c[5]!=0):
	if(c[5]<0):
		negate = True
		finallist = Con2Bal.doIt(c[5]*-1)
	else:
		finallist = Con2Bal.doIt(c[5])
	#print(negate)
	if(negate):
		#print(finallist)
		for i in range(6):
			if(finallist[i]==1):
				finallist[i]='Z'
				continue
			if(finallist[i]=='Z'):
				finallist[i]=1
				continue
			if(finallist[i]==0):
				continue
				
	finalstring = []
	finalcolors=doColors(3)
	fullfinallist=[]
	if(len(finallist)<6):
		for i in range(6-len(finallist)):
			fullfinallist.append(0)
		for i in finallist:
			fullfinallist.append(i)
	else:
		fullfinallist=finallist
	for i in range(6):
		if(fullfinallist[i]==1):
			finalstring.append(f'+{finalcolors[i]}')
			continue
		elif(fullfinallist[i]=='Z'):
			finalstring.append(f'-{finalcolors[i]}')
			continue
		else:
			continue

	print(c)
	clearScreen()
	input(''.join(finalstring))
else:
	clearScreen()
	input('The answer is 0!')
