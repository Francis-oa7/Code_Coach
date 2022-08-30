message = 'd89%l++5r19o7W *o=l645le9H'
a = message[::-1].split()
for i in a:
 a = (chr for chr in i if chr.isalpha())
 print(''.join(a),end=" ")
 # Works fine