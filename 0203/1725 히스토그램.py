import sys
input = sys.stdin.readline

n = int(input())
hist = [int(input()) for _ in range(n)]

MAP = [[0] * n for _ in range(max(hist))]

for i in range(len(MAP[0])):
    for j in range(len(MAP)-hist[i], len(MAP)):
        MAP[j][i] = hist[i]

for i in MAP:
    print(i)