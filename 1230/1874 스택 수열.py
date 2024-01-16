import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]

stack = []
idx = 1
answer = []

for i in numbers:

    while idx <= i:
        stack.append(idx)
        idx += 1
        answer.append("+")

    if stack[-1] == i:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        exit()

for i in answer:
    print(i)