import sys
input = sys.stdin.readline
n = int(input())

def minHeap(k):
    if k // 2 == 0: return
    if heap[k] < heap[k//2]:
        heap[k], heap[k//2] = heap[k//2], heap[k]
        minHeap(k//2)
    
def maxHeap(k):
    sw = k*2
    if sw > k: return
    if sw+1 <= k and heap[sw] > heap[sw+1]:
        sw += 1
    if heap[k] > heap[sw]:
        heap[k], heap[sw] = heap[sw], heap[k]
        maxHeap(sw)

heap= [0]
k = 0
for _ in range(n):
    x = int(input())

    if k == 0 and x == 0:
        print(0)
    elif x > 0:     # 자연수면 값 추가
        heap.append(x)
        k+=1
        minHeap(k)
    else:           # 음수면 최소값 제거
        maxHeap(1)
        heap[1], heap[-1] = heap[-1], heap[1]
        print(heap.pop())
        k-=1