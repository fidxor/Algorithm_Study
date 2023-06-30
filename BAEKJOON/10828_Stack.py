from collections import deque
import sys 

N = int(input())

numlst = deque()

for i in range(N):
    inputCmd = sys.stdin.readline().rstrip()
    
    if inputCmd == 'pop':
        if numlst: print(numlst.pop()) 
        else: print(-1)         
    elif inputCmd == 'size':
        print(len(numlst))
    elif inputCmd == 'empty':
        if numlst: print(0)
        else: print(1)
    elif inputCmd == 'top':     
        if numlst: print(numlst[-1])
        else: print(-1)
    else:                
        numbers = inputCmd.split()        
        numlst.append(int(numbers[1]))

