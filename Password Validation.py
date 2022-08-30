Password = input('Password:')
s = 0
n = 0
l = len(Password)
for i in Password:
 if i.isnumeric():
     n+=1
 elif i.isalnum() == False:
     s+=1
def validate():
  if l >= 7 and s >= 2 and n >= 2:
      return 'Strong'
  else:
      return 'Weak'
print(validate())
#Works fine                     