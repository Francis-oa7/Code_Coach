import numpy as np
nums = np.array([2,6,5,3,1,4])
target = 7

for i in range(len(nums)):
    a = nums[i] + nums
    if target in a:
        a = list(a)
        if i != a.index(target):
            break
        else:
         continue
print([i,a.index(target)])
#q = [int(x) for x in'[2,3,4]'.strip('[]').split(',')]
