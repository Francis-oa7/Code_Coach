import math

phrase = input().split()
len_w = len(phrase)
s = 0

for i in phrase :
  if i.isalpha():
  
    s = s + len(i)
 
l = s/len_w 

print(math.ceil(l))