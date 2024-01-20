import sys
input = sys.stdin.readline

n, m = map(int, input().split())
M = 500009
hash = [[] for _ in range(M)]
monster_list = []

for i in range(n):
    monster = input().strip()
    monster_list.append(monster)
    num = 0
    for j, s in enumerate(monster):
        num += (ord(s) - 64) * 53 ** j

    hash[num % M].append([i+1, monster])

for i in range(m):
    monster = input().strip()
    
    if monster.isnumeric():
        print(monster_list[int(monster)-1])
    else:
        num = 0
        for j, s in enumerate(monster):
            num += (ord(s) - 64) * 53 ** j

        for k in hash[num % M]:
            if k[1] == monster:
                print(k[0])
                break