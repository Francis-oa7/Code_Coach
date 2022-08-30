sales = int(input("Monthly sales:"))
p = sales * 3000000
if p > 21000000:
 print("Profit")
else:
 if p < 21000000:
   print('Loss')
 else:
    if p == 21000000:
     print('Broken even')      