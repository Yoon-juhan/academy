x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def ccw(x1, x2, x3, y1, y2, y3):
    return (x1* y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

a = ccw(x1, x2, x3, y1, y2, y3)
b = ccw(x1, x2, x4, y1, y2, y4)
c = ccw(x3, x4, x1, y3, y4, y1)
d = ccw(x3, x4, x2, y3, y4, y2)

n, m = a * b, c * d

if n == 0 and m == 0:
    if (min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4)):
        print(1)
    else:
        print(0)
elif n <= 0 and m <= 0:
    print(1)
else:
    print(0)