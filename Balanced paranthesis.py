def balanced(exp):
    p = []
    for i in exp:
     if (i == '(') or (i == '[') or (i =='{'):
          p.insert(0,i)
     elif (i == ')' and '(' in p) or (i == ']' and '[' in p) or (i == '}' and '{' in p):
         if i == ')':
          p.remove('(')
         elif i == ']':
          p.remove('[')
         elif i == '}':
          p.remove('{')  
     else:
         return False           
    if len(p) != 0:
        return False
    else:
        return True          
                 
print(balanced('(])]'))  
# Works fine :-)