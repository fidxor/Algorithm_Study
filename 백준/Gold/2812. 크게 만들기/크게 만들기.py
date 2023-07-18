K, N = map(int, input().split())
num = input()

resultlst = []
deletecnt = 0

for i in range(K):
    if i == 0:
        resultlst.append(num[i])
        continue
       
    
    while N > 0:
        if resultlst[-1] < num[i]:
            N -= 1
            resultlst.pop()
            if not resultlst:
                resultlst.append(num[i])
                break            
            continue        
        resultlst.append(num[i])
        break

    if N == 0:
        resultlst.append(num[i:])
        break

if N > 0:
    resultlst = resultlst[:len(resultlst) - N]

print(int(''.join(resultlst)))