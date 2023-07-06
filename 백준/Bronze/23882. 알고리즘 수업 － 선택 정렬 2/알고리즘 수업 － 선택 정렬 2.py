lst = list(map(int, input().split()))

def SelectSort(N, K):

    numlst = list(map(int, input().split()))

    lastindex = N - 1
    cnt = 0

    for i in numlst:
        maxidx = numlst.index(max(numlst[:lastindex + 1])) # 정렬이 완료된건 제외하고 가장 높은 수를 찾는다

        if(numlst[maxidx] != numlst[lastindex]):
            numlst[lastindex], numlst[maxidx] = numlst[maxidx], numlst[lastindex]
            cnt += 1
        
        lastindex -= 1

        if cnt == K:
            break        
            
    if cnt < K:
        print(-1)
    else:
        print(*numlst) # [2, 1, 3, 4, 5] 이렇게 출력되던걸 2 1 3 4 5 이렇게 출력되도록

SelectSort(lst[0], lst[1])