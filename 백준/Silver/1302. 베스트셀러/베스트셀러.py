import sys

N = int(input())

books = dict()

for i in range(N):
    book = sys.stdin.readline().rstrip()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

books = dict(sorted(books.items(), key=lambda x : (-x[1], x[0])))

print(list(books.keys())[0])