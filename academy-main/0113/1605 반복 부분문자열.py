L = int(input())
string = input()

M = 50009
r = 31

def hashing(s):
    for idx, s in enumerate(s):
        num += (ord(s) - 96) * r ** idx
    return num % M

l, r = 0, L
while l <= r:
    hash = ["" for _ in range(M)]
    mid = (l + r) // 2

    st = string[:mid]   # 처음 문자
    num = hashing(st)
    hash[num] = st
    for i in range(L-mid):
        num += hashing(string[mid+i])
        num -= hashing(string[i])
        if hash[num]:    # 문자열이 있으면
            l = mid + 1
            break
        else:
            hash[num] = st
    else:
        r = mid - 1

print(mid)