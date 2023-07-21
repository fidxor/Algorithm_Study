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
    # 앞에서 자를거 다 잘랐으면 뒤에 남은거 전부 한번에 붙인다.
    if N == 0:
        resultlst.append(num[i:])
        break
# 다 붙였는데 N이 0이 아니면 N만큼 뒤에 날려준다.
if N > 0:
    resultlst = resultlst[:len(resultlst) - N]

print(int(''.join(resultlst)))