from collections import deque

M = 50009
r = 11

puzzle = [list(map(int, input().split())) for _ in range(3)]

# 정답 해시값
answer_hash = 0     # 43444
for i in range(1, 9):
    answer_hash += i * r ** i
answer_hash %= M

def getHash():
    hash = 0
    for i in range(4):
        for j in range(4):
            hash += i * r ** i
    if hash == answer_hash:
        print(cnt)
        return
    
    return hash % M

q = deque([(0, 0, 0)])
visit = [0] * M
visit[getHash()] = 1

while q:
    now_x, now_y, cnt = q.popleft()

    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    for i in range(4):
        next_x, next_y = now_x + dx[i], now_y + dy[i]

        if 0 <= next_x < 4 and 0 <= next_y < 4 and puzzle[next_x][next_y] == 0:
            puzzle[now_x][now_y], puzzle[next_x][next_y] = puzzle[next_x][next_y], puzzle[now_x][now_y]
            if not visit[getHash()]:
                visit[getHash()] = 1
                q.append((next_x, next_y, cnt+1))
                puzzle[next_x][next_y], puzzle[now_x][now_y] = puzzle[now_x][now_y], puzzle[next_x][next_y]

            for i in puzzle:
                print(i)
