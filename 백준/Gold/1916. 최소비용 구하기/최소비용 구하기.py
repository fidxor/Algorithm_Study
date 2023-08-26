import sys 
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())
M = int(input())
price = [sys.maxsize] * (N + 1)  # 버스비용 저장 리스트
visited = [False] * (N + 1)     # 방문했는지 확인 여부 리스트
myList = [[] for _ in range(N + 1)]     # 인접 리스트
q = PriorityQueue()     # 다익스트라를 위한 우선순위 큐

# 인접리스트에 에지 정보 저장
for _ in range(M):
    u, v, w = map(int, input().split())
    myList[u].append((v, w))

'''
문제에서 입력값 중에 마지막줄의 입력값은 출발점과 도착점을 갈수 있는 경우에만 입력 값으로 주어진다고 한다.
즉 입력값이 없을수도 있다는 소리...

Exception has occurred: ValueError
not enough values to unpack (expected 2, got 0)
  File "D:\Programing Study\Algorithm_Study\BAEKJOON\1916_최소비용구하기.py", line 22, in <module>
    startNode, endNode = map(int, input().split())
    ^^^^^^^^^^^^^^^^^^
ValueError: not enough values to unpack (expected 2, got 0)

sys.stdin.readline 을 사용했을 경우 입력값이 없을 경우 위에 에러가 발생하기 때문에 
python의 경우 try: except: 문을 사용해서 처리 해야 한다.
'''

try:
    startNode, endNode = map(int, input().split())

    q.put((0, startNode))       # 출발노드는 우선순위 큐에 넣고 시작
    price[startNode] = 0     # 비용 리스트에 출발노드의 값을 0으로 설정

    while q.qsize() > 0:
        current = q.get()       # 우선순위 큐에서 노드 가져오기
        if visited[current[1]]: # 방문한 노드면 continue
            continue

        visited[current[1]] = True  # 현재 노드를 방문한 노드로 업데이트

        for tmp in myList[current[1]]:
            next = tmp[0]   # 다음 인접노드
            value = tmp[1]  # 다음 인접노드의 비용

            # 연결노드 비용리스트값보다 선택노드의 비용리스트값 + 에지가중치가 더 작은 경우 업데이트를 한다
            if price[next] > price[current[1]] + value: 
                price[next] = price[current[1]] + value
                q.put((price[next], next))  # 업데이트가 되면 연결된 노드를 우선순위큐에 넣는다.


    print(price[endNode])   # 도착노드의 비용을 출력
except:
    print("0")  # 출발노드와 도착노드값이 입력으로 없으면 0을 출력