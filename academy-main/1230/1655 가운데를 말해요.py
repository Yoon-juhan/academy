import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())

num = int(input())
print(num)
minHeap, maxHeap = [],[-num]

for i in range(n-1):
    num = int(input())
    if num > -maxHeap[0]:
        heappush(minHeap, num)
    else:
        heappush(maxHeap, -num)
        
    if len(minHeap) > len(maxHeap):
        temp = heappop(minHeap)
        heappush(maxHeap, -temp)
    elif len(minHeap)+1 < len(maxHeap):
        temp = heappop(maxHeap)
        heappush(minHeap, -temp)

    print(-maxHeap[0])