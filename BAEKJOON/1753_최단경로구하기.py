import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())
K = int(input())
distance = [sys.maxsize] * (V + 1)  # 거리저장 리스트 1부터 시작하기 때문에 +1 해줌
visited = [False] * (V + 1)     # 방문여부 저장 리스트 
myList = [[] for _ in range(V + 1)] # 에지 데이터 인접 리스트
q = PriorityQueue()         # 다익스트라를 위한 우선순위 큐

# 에지 개수만큼 반복해서 인접리스트 만들
for _ in range(E):
    u, v, w = map(int, input().split()) 
    myList[u].append((v, w))        # 인접리스트에 에지정보 저장

q.put((0, K))   # 출발노드를 우선순위 큐에 넣고 시작
distance[K] = 0 # 거리 리스트에 출발노드의 값을 0으로 설정

# 우선순위 큐가 빌때까지 반복
while q.qsize() > 0:
    current = q.get()   # 우선순위 큐에서 노드 가져오기
    c_v = current[1]    
    if visited[c_v]:    # 현재 선택된 노드를 방문한적이 있는지 확인
        continue

    visited[c_v] = True # 현재 노드를 방문한 노드로 업데이트
    for tmp in myList[c_v]: # 현재 선택된 노드의 에지개수
        next = tmp[0]   # 다음 노드
        value = tmp[1]  # 다음 노드의 거리

        # 연결 노드의 최단거리 > 연결 노드 방문 전 AND 현재 선택 노드의 최단거리 + 비용
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value  # 연결노드 최단거리 업데이트
            q.put((distance[next], next))       # 우선순위 큐에 연결노드 추가

for i in range(1, V + 1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")