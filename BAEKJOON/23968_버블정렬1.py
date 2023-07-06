'''
bubble_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for last <- N downto 2
        for i <- 1 to last - 1
            if (A[i] > A[i + 1]) then A[i] <-> A[i + 1]  # 원소 교환
}
'''

lst = list(map(int, input().split()))

def BubbleSort(N, K):
    numlst = list(map(int, input().split()))
    resultlst = []

    lastindex = N - 1
    cnt = 0

    index = 0

    while True:
        if numlst[index] > numlst[index + 1]:
            numlst[index], numlst[index + 1] = numlst[index + 1], numlst[index]
            cnt += 1
            if cnt == K:
                resultlst = [numlst[index], numlst[index + 1]]
                print(*resultlst)
                break
        
        index += 1

        if index >= (N - 1):
            N -= 1
            index = 0
            if N <= 0:
                break

    if cnt < K:
       print(-1)

BubbleSort(lst[0], lst[1])

# for last in range(lastindex):        
    #     for i in range(N - 1):
    #         if numlst[i] > numlst[i + 1]:
    #             numlst[i], numlst[i + 1] = numlst[i + 1], numlst[i]
    #             cnt += 1
    #             lastindex -= 1
    #             if cnt == K:
    #                 resultlst = [numlst[i], numlst[i + 1]]
    #                 print(*resultlst)
    #                 return 


'''
시간 초과
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

------------------------------------------------------------------------------

lst = list(map(int, input().split()))

def BubbleSort(N, K):
    numlst = list(map(int, input().split()))
    resultlst = []

    lastindex = N - 1
    cnt = 0

    for last in range(lastindex):        
        for i in range(N - 1):
            if numlst[i] > numlst[i + 1]:
                numlst[i], numlst[i + 1] = numlst[i + 1], numlst[i]
                cnt += 1
                lastindex -= 1
                if cnt == K:
                    resultlst = [numlst[i], numlst[i + 1]]
                    print(*resultlst)
                    return            

    if cnt < K:
       print(-1)

BubbleSort(lst[0], lst[1])

---------------------------------------------------------------------------

lst = list(map(int, input().split()))

def BubbleSort(N, K):
    numlst = list(map(int, input().split()))
    resultlst = []

    lastindex = N - 1
    cnt = 0

    arr = numlst.copy()
    
    arr.sort()

    for last in numlst:
        if arr == numlst:
            break
        for i in range(lastindex):
            if arr == numlst:
                break
            if numlst[i] > numlst[i + 1]:
                numlst[i], numlst[i + 1] = numlst[i + 1], numlst[i]
                cnt += 1
                if cnt == K:
                    resultlst = [numlst[i], numlst[i + 1]]
                    print(*resultlst)
                    return

    if cnt < K:
       print(-1)

BubbleSort(lst[0], lst[1])

--------------------------------------------------------------------------

lst = list(map(int, input().split()))

def BubbleSort(N, K):
    numlst = list(map(int, input().split()))
    resultlst = []

    lastindex = N - 1
    cnt = 0

    index = 0

    while True:
        if numlst[index] > numlst[index + 1]:
            numlst[index], numlst[index + 1] = numlst[index + 1], numlst[index]
            cnt += 1
            if cnt == K:
                resultlst = [numlst[index], numlst[index + 1]]
                print(*resultlst)
                break
        
        index += 1

        if index >= (N - 1):
            N -= 1
            index = 0
            if N <= 0:
                break

    if cnt < K:
       print(-1)

BubbleSort(lst[0], lst[1])
'''
