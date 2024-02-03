n, m, k = map(int, input().split())

s = 0
i = 1
while True:
     if n <= 2 ** i:
        s = 2 ** i
        break
     i += 1

tree = [0] * (s*2)  # 트리 크기

def update(n):
   if n < 1: return
   tree[n] = tree[n*2] + tree[n*2+1]
   update(n//2)

for i in range(n):
    x = int(input())
    now = s + i
    tree[now] = x
    update(now//2)

print(tree)