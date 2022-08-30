import numpy as np
players = [180,172,178,185,190,195,192,200,210,190]
a = np.array(players)
s = np.std(a)
m = np.mean(a)
print(s,m)
print(type(a))
f = int(m - s)
l = int(m+s) + 1
c = 0
r = list(range(f,l))
print(r)
for i in players:
    if i in r:
        c+=1
print(c-1)