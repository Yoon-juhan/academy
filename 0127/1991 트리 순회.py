n = int(input())

tree = {}
for _ in range(n):
    a, b, c = input().split()
    tree[a] = [b, c]

answer1 = []
answer2 = []
answer3 = []

def dfs(now):

    if now != '.':
        answer1.append(now)
        dfs(tree[now][0])
        answer2.append(now)
        dfs(tree[now][1])
        answer3.append(now)

dfs('A')

print("".join(answer1))
print("".join(answer2))
print("".join(answer3))