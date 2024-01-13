n = int(input())

numbers = [int(input()) for _ in range(n)]

def merge(a, b, c, d):
    tmp = []
    i = x = a

    while a <= b and c <= d:
        if numbers[a] < numbers[c]:
            tmp.append(numbers[a])
            a += 1
        else:
            tmp.append(numbers[c])
            c += 1
    
    if a <= b:
        for i in range(a, b+1):
            tmp.append(numbers[i])
    else:
        for i in range(c, d+1):
            tmp.append(numbers[i])

    for i in range(len(tmp)):
        numbers[x+i] = tmp[i]

def mergesort(l, r):
    if l == r:
        return
    
    mid = (l + r) // 2
    mergesort(l, mid)
    mergesort(mid+1, r)

    merge(l, mid, mid+1, r)
    
mergesort(0, n-1)

for i in numbers:
    print(i)