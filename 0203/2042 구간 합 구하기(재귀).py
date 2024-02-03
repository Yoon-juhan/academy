import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

s = 1
while s <= n:
    s *= 2

tree = [0] * (s*2)

def init(start, end, idx):
    if start == end:
        tree[idx] = numbers[start-1]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx*2) + init(mid+1, end, idx*2+1)
    return tree[idx]

def update(start, end, idx):
    if start > b or end < b:
        return tree[idx]
    if start == end and start == b:
        tree[idx] = numbers[start-1]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx*2) + init(mid+1, end, idx*2+1)
    return tree[idx]

def query(start, end, idx):
    if start > c or end < b:
        return 0
    if b <= start and c >= end:
        return tree[idx]
    
    mid = (start + end) // 2
    tree[idx] = query(start, mid, idx*2) + query(mid+1, end, idx*2+1)
    return tree[idx]

init(1, n, 1)   # 세그먼트 트리 세팅

for _ in range(k*2):
    a, b, c = map(int, input().split())
    if a == 1:
        numbers[b-1] = c
        update(1, n, 1)
    else:
        print(query(1, n, 1))