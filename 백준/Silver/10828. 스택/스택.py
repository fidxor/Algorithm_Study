import sys 

N = int(input())

numlst = []

for i in range(N):
    inputCmd = sys.stdin.readline().rstrip()
    
    if inputCmd == 'pop':
        if len(numlst) >= 1: print(numlst.pop()) 
        else: print(-1)         
    elif inputCmd == 'size':
        print(len(numlst))
    elif inputCmd == 'empty':
        if len(numlst) >= 1: print(0)
        else: print(1)
    elif inputCmd == 'top':     
        if len(numlst) >= 1: print(numlst[-1])
        else: print(-1)
    else:                
        numbers = inputCmd.split()        
        numlst.append(int(numbers[1]))

