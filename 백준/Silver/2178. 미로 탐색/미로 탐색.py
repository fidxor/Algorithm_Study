import sys
from collections import deque

input = sys.stdin.readline
q = deque()

N, M = map(int, input().split())

# 미로 맵을 만들어 준다.
map = []
for _ in range(N):
    inputtext = input().rstrip()
    mapline = [int(x) for x in inputtext]
    map.append(mapline)


curProgress = 1     # 현재 어디까지 진행 됐는지 체크하는 값
startPos = [0, 0, curProgress]  # startPosition에 첫 0, 0 좌표와 진행 값을 넣어준다.
endPos = [N - 1, M - 1]

q.append(startPos)  # 큐에 현재 포지션 값 넣어주기

mapHeight = len(map) - 1
mapWidth = len(map[0]) - 1

while len(q) > 0:
    # 도착지의 숫자가 바뀌면 반복문 빠져나가기
    if map[endPos[0]][endPos[1]] != 1:
        break
    
    curPos = q.popleft()
    curX, curY, curWIP = curPos
    # 현재 포지션에서 상, 하, 좌, 우로 이동할수 있으면
    # 포지션값 바꿔주고 우선순위큐에 넣어주기
    if map[max(curX - 1, 0)][curY] == 1:    # 상
        map[max(curX - 1, 0)][curY] = curWIP + 1    
        q.append([max(curX - 1, 0), curY, curWIP + 1])

    if map[min(curX + 1, mapHeight)][curY] == 1:    # 하
        map[min(curX + 1, mapHeight)][curY] = curWIP + 1
        q.append([min(curX + 1, mapHeight), curY, curWIP + 1])
        
    if map[curX][max(curY - 1, 0)] == 1:    # 좌
        map[curX][max(curY - 1, 0)] = curWIP + 1
        q.append([curX, max(curY - 1, 0), curWIP + 1])

    if map[curX][min(curY + 1, mapWidth)] == 1: # 우
        map[curX][min(curY + 1, mapWidth)] = curWIP + 1
        q.append([curX, min(curY + 1, mapWidth), curWIP + 1])
    
print(map[endPos[0]][endPos[1]])