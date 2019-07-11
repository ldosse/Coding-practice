import time
start = time.time()
p="aaabbaaa"
l=len(p)
s=p[0]
for i in range(l-1,0,-1):
    if p[i]==s:
        if p[i:]==p[0:l-1-i+1]:
            print(p[i:])
end = time.time()
print(end - start)
suf=""
pre=""
for i in range(l-1,1,-1):
    suf = p[i]+suf
    pre = pre+p[l-i-1]
    if pre==suf:
        print(suf)

s=""
pr=""
for i in range(l-1):
    pr=p[0:i+1]
    s=p[l-i-1:]
    if pr==s:
        print(pr)
