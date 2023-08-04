import sys

N, M = map(int, input().split())

words = dict()

for i in range(N):
    word = sys.stdin.readline().rstrip()
    if(len(word) < M):
        continue

    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

words = dict(sorted(words.items(), key=lambda x : (-x[1], -len(x[0]), x[0])))

for word in list(words.keys()):
    print(word)