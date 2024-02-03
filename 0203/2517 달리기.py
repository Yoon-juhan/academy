import sys
input = sys.stdin.readline

n = int(input())
numbers = sorted([(int(input()), i+1) for i in range(n)])
print(numbers)

tree = [0] * (2**20)
