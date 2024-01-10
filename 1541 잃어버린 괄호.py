n = input()

s = n.split('-')

for i in range(len(s)):
    if '+' in s[i]:
        tmp = map(int, s[i].split('+'))
        s[i] = sum(tmp)
    else:
        s[i] = int(s[i])
    
answer = s[0]
for i in range(1, len(s)):
    answer -= s[i]
    
print(answer)