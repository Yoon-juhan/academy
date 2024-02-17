n = int(input())

rec = []
x = []
y = []
for i in range(n):
    a, b, c, d = map(float, input().split())
    x.append(a)
    x.append(a+c)
    y.append(b)
    y.append(b+d)
    rec.append((a, b, a+c, b+d))

x.sort()
y.sort()

answer = 0
for i in range(len(x)-1):
    x1, x2 = x[i], x[i+1]
    if x1 == x2:
        continue
    for j in range(len(y)-1):
        y1, y2 = y[j], y[j+1]

        if y1 == y2:
            continue
        else:
            for r in rec:
                if x1 >= r[0] and y1 >= r[1] and x2 <= r[2] and y2 <= r[3]:
                    answer += (x2 - x1) * (y2 - y1)
                    break

if int(answer) == answer:
    print(int(answer))
else:
    print(f"{answer:.2f}")