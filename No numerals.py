import string
text = str(input("text:"))
c = string.hexdigits

for i in text:
   if i == '10':
      text = text.replace('10','ten') 
   if i == '9':
      text = text.replace('9','nine')  
   if i == '8':
      text = text.replace('8','eight')   
   if i == '7':
      text = text.replace('7','seven')
   if i == '6':
      text = text.replace('6','six')
   if i == '5':
      text = text.replace('5','five')
   if i == '4':
      text = text.replace('4','four')
   if i == '3':
      text = text.replace('3','three')
  
   if i == '2':
      text = text.replace('2','two')
   if i == '1':
      text = text.replace('1','one')
   if i == '0':
      text = text.replace('0','zero')    
                            

print(str(text))
print(c)

    