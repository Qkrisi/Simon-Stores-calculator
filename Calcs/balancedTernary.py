#Code contributed by Rituraj Jain modified by Qkrisi
#Original code: https://www.geeksforgeeks.org/game-theory-in-balanced-ternary-numeral-system-moving-3k-steps-at-a-time/

arr = [0] * 32
  
def balTernary(ter):  
   
    carry, base, i = 0, 10, 31 
    while ter > 0: 
        rem = (ter % base) + carry  
          
        if rem == 0:   
            arr[i] = 0 
            carry, i = 0, i-1 
           
        elif rem == 1:   
            arr[i] = 1 
            carry, i = 0, i-1 
           
        elif rem == 2:   
            arr[i] = -1 
            carry, i = 1, i-1 
           
        elif rem == 3:   
            arr[i] = 0 
            carry, i = 1, i-1 
           
        ter = ter // base  
       
    if carry == 1: 
        arr[i] = 1 
   

def ternary(number):  
   
    ans, rem, base = 0, 1, 1 
    while number > 0: 
        rem = number % 3 
        ans = ans + rem * base  
        number //= 3 
        base = base * 10 
       
    return ans  
   
 
def doIt(num):
    print(num)
    number = num
    ter = ternary(number)
    balTernary(ter)
    full=[]
    final=[]
    i = 0 
  

    while arr[i] == 0:   
        i += 1
       

    for j in range(i, 32):   
  

        if arr[j] == -1:  
            full.append('Z')
        else: 
            full.append(arr[j])
    #print(full)
    if(len(full)<6):
        for i in range(6-len(full)):
            final.append(0)
    for i in full:
        final.append(i)
    final.reverse()
    print(final)
    return final

#print(doIt(118))
