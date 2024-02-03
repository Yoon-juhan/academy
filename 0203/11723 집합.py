import sys
input = sys.stdin.readline

n = int(input())

check = 0

for i in range(n):
    q = input().strip().split(" ")
    if q[0] == "add":
        x = int(q[1]) - 1
        check = check | (1 << x)
    elif q[0] == "remove":
        x = int(q[1]) - 1
        check = check & ~(1 << x)
    elif q[0] == "check":
        x = int(q[1]) - 1
        if check & (1 << x):
            print(1)
        else:
            print(0)
    elif q[0] == "toggle":
        x = int(q[1]) - 1
        check = check ^ (1 << x)
    elif q[0] == "all":
        check = (1 << 20) - 1
    else:
        chkek = 0