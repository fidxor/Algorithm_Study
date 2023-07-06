lst = list(map(int, input().split()))

def SelectSort(N, K):

    numlst = list(map(int, input().split()))

    lastindex = N - 1
    cnt = 0

    for i in numlst:
        maxidx = numlst.index(max(numlst[:lastindex + 1]))

        if(numlst[maxidx] != numlst[lastindex]):
            numlst[lastindex], numlst[maxidx] = numlst[maxidx], numlst[lastindex]            
            cnt += 1
        
        lastindex -= 1

        if cnt == K:
            break        
            
    if cnt < K:
        print(-1)
    else:
        print(*numlst)

SelectSort(lst[0], lst[1])