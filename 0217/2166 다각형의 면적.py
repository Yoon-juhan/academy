n = int(input())

def ccw(x1, x2, x3, y1, y2, y3):
    return (x1* y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

x0, y0 = map(int, input().split())
coordinate = []

for i in range(n-1):
    coordinate.append(list(map(int, input().split())))

s = 0

for i in range(len(coordinate)-1):
    s += (ccw(x0, coordinate[i][0], coordinate[i+1][0], y0, coordinate[i][1], coordinate[i+1][1])) / 2

print(abs(s))