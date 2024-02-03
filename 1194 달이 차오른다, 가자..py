n, m = map(int, input().split())

MAP = [list(input()) for _ in range(n)]

key = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6
}

for i in MAP:
    print(i)