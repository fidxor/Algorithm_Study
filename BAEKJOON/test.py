# K, N = map(int, input().split())
# num = int(input())

K, N  = 10, 3
num = "2222211113"

numstr = str(num)
resultlst = []
deletecnt = 0

for i in range(K):
    if not resultlst:            
        resultlst.append(numstr[i])
    else:
        tempnum = numstr[i]
        while True:
            if not resultlst:
                resultlst.append(tempnum)
                break

            if deletecnt >= N:
                resultlst.append(tempnum)
                break
            if int(resultlst[-1]) < int(tempnum):
                if(deletecnt < N):
                    resultlst.pop()
                    deletecnt += 1
                else:
                    resultlst.append(tempnum)
                    break

print(int(''.join(resultlst)))