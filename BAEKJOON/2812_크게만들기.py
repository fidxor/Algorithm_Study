'''
문제
N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.

출력
입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.
'''

# K, N = map(int, input().split())
# num = int(input())

K, N  = 10, 3
num = "2222211113"

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


'''
K, N = 10, 4
num = 4177252841

K, N  = 6, 3
num = "773671"
'''
# if i == 0:            
#     resultlst.append(numstr[i])
#     continue
# if deletecnt >= N:
#     resultlst.append(numstr[i:])
#     break
# else:
#     tempnum = numstr[i]
#     while True:
#         if len(resultlst) <= 0:
#             resultlst.append(tempnum)
#             break
#         if deletecnt >= N:
#             resultlst.append(tempnum)
#             break                                
#         if resultlst[-1] < tempnum:
#             if(deletecnt < N):
#                 resultlst.pop()
#                 deletecnt += 1            
#         else:
#             resultlst.append(tempnum)
#             break