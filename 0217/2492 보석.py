n, m, t, k = map(int, input().split())

x = []
y = []
answer_x = 0
answer_y = 0
answer = 0
for i in range(t):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(len(x)):
    x1, x2 = x[i], x[i] + k
    for j in range(len(y)):
        y1, y2 = y[j] - k, y[j]
        cnt = 0
        for t in range(t):
            if x1 <= x[t] and x2 >= x[t] and y1 <= y[t] and y2 >= y[t]:
                cnt += 1
        if answer < cnt:
            answer = cnt
            answer_x = min(x1, n-k)
            answer_y = max(y2, k)

print(answer_x, answer_y)
print(answer)