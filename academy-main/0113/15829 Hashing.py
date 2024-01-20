r = 31
M = 1234567891
answer = 0

l = int(input())
string = input()

for i, s in enumerate(string):
    answer += (ord(s) - 96) * r ** i

print(answer % M)