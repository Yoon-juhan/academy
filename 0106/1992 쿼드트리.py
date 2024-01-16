n = int(input())

MAP = [list(map(int, input())) for _ in range(n)]

def quad(x, y, length):
    if length == 1:
        print(MAP[x][y], end="")
        return
            
    now = MAP[x][y]
    sw = False

    for i in range(x, x + length):
        for j in range(y, y + length):
            if MAP[i][j] != now:
                sw = True
                break
        if sw:
            break
    if not sw:
        print(now, end="")
        return

    print("(", end="")

    quad(x, y, length // 2)                              # 왼쪽 위
    quad(x, y + length // 2, length // 2)                # 오른쪽 위
    quad(x + length // 2, y, length // 2)                 # 왼쪽 아래
    quad(x + length // 2, y + length // 2, length // 2)   # 오른쪽 아래

    print(")", end="")

quad(0, 0, n)