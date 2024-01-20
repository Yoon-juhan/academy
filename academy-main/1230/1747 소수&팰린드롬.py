n = int(input())

prime = [True] * (1_030_001)
prime[1] = False

for i in range(2, int(1_030_000 ** 0.5) + 1):
    if prime[i]:
        for j in range(i*2, 1_030_000 + 1, i):
            prime[j] = False

for i in range(n, len(prime)):
    if prime[i]:
        if str(i) == str(i)[::-1]:
            print(i)
            exit()