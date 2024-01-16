import sys
input = sys.stdin.readline

n, m = map(int, input().split())
M = 500009
hash = [[0, ""]] * M
monster_list = []

for i in range(n):
    monster = input().strip()
    monster_list.append(monster)
    num = 0
    for j, s in enumerate(monster):
        num += (ord(s) - 64) * 53 ** j

    hash[num % M][0] = i+1
    hash[num % M][1] = monster
    print(hash[num % M], num % M)

for i in range(m):
    monster = input().strip()
    
    if monster.isnumeric():
        print("출력 = ", monster_list[int(monster)-1])
    else:
        num = 0
        for j, s in enumerate(monster):
            num += (ord(s) - 64) * 53 ** j

        print("출력 = ", hash[num % M][0])