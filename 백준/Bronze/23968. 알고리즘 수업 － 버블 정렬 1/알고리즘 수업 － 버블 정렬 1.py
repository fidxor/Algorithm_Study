lst = list(map(int, input().split()))

def BubbleSort(N, K):
    numlst = list(map(int, input().split()))
    resultlst = []

    lastindex = N - 1
    cnt = 0

    for last in numlst:
        for i in range(lastindex):
            if numlst[i] > numlst[i + 1]:
                numlst[i], numlst[i +1] = numlst[i +1], numlst[i]
                cnt += 1
                if cnt == K:
                    resultlst = [numlst[i], numlst[i +1]]
                    print(*resultlst)
                    return
                
    if cnt < K:
        print(-1)

BubbleSort(lst[0], lst[1])

# 백준에 굴복하고 말았다.