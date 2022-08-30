x = int(input())
s = 0
c = 0
while s < x:
   y = int(input())
   s += 1
   if y % 2 != 0:
      continue
   else:
     c += y
print(c)      

