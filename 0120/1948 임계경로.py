from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())