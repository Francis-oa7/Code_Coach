import numpy as np
n,p = [int(x) for x in input().split()]
d = []
for i in range(n):
 s = [float(w) for w in input().split()]
 d.append(s)
d_arr = np.array(d)
r_mean = d_arr.mean(axis=1)
print(np.round_(r_mean,2))

# works fine