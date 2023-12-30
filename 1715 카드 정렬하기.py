import sys

input = sys.stdin.readline
n = int(input())

def up(k):
    if k // 2 == 0:
        return
    if heap[k] < heap[k // 2]:
        heap[k], heap[k // 2] = heap[k // 2], heap[k]
        up(k // 2)

def down(k):
    sw = k * 2
    if sw > k:
        return
    if sw + 1 <= k and heap[sw] > heap[sw + 1]:
        sw += 1
    if heap[k] > heap[sw]:
        heap[k], heap[sw] = heap[sw], heap[k]
        down(sw)


heap = [0] * (n + 1)
k = n
answer = 0

for i in range(1, n + 1):
    heap[i] = int(input())

heap.sort()

while True:
    if(k==1): break
    tmp = 0
    for _ in range(2):
        tmp += heap.pop(1)
        down(1)
        k -= 1
        
    heap.append(tmp)
    k += 1
    up(k)
    answer += tmp

print(answer)