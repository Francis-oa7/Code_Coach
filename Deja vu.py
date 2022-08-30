word = input()
a = 'Unique'
b = 'Deja vu'
def func_(x):

 for i in x:
    
    if x.count(i) > 1:
      return b
 return a
    
print(func_(word))         
