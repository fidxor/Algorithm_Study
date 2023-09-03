import heapq

def solution(scoville, K):
    answer = 0 
    # scoville리스트를 힙정렬한다.   
    heapq.heapify(scoville)

    # scoville 리스트 안에 하나라도 K 보다 작은 값이 있으면 반복 
    while any(K > x for x in scoville):
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 
        if (len(scoville) <= 1):
            answer = -1
            break

        firstVal = heapq.heappop(scoville)
        secondVal = heapq.heappop(scoville)

        newVal = firstVal + (secondVal * 2)

        heapq.heappush(scoville, newVal)

        answer += 1

    return answer