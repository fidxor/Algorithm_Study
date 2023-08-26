# user_input = input()
# userCards = list(map(int, input().split()))

# cards = dict()


### 2번 문제
# for card in userCards:
#     if card not in cards:
#         cards[card] = 1
#     else:
#         cards[card] += 1

# cards = dict(sorted(cards.items(), key=lambda x : x[1]))

# print(list(cards.keys())[0])


### 3번 문제
# import sys
# import datetime
# N, K = map(int, input().split())

# timeDict = dict()

# for i in range(N):
#     inoutTime = sys.stdin.readline().rstrip()
#     name, time = inoutTime.split()
#     time = datetime.datetime.strptime(time, '%H:%M')    
#     timelst = []
#     timelst.append(time)

#     if name not in timeDict:
#         timeDict[name] = timelst
#     else:
#         timeDict[name] += timelst

# count = 0
# for times in timeDict.values():
#     totaltime = 0    
#     for i in range(0, len(times), 2):
#         time = times[i + 1] - times[i]
#         totaltime += time.seconds / 60 / 60
    
#     if totaltime >= K:
#         count += 1

# print(count)
    

### 4번 문제
# import sys

# N, K = map(int, input().split())

# wordlst = list()

# for i in range(N):
#     word = sys.stdin.readline().rstrip()
#     wordlst.append(word)

# wordlst = sorted(wordlst, key=lambda x : (len(x), x))

# print(wordlst[K - 1])