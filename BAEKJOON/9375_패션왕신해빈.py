import sys

N = int(input())

for i in range(N):
    K = int(sys.stdin.readline())
    for j in range(K):
        inputWear = sys.stdin.readline().split()
        print(inputWear)
