date = input('Date(MM/DD/YYYY):').capitalize()
month = ['January','February','March','April','May','June','July','August','September','October','November','December']
month1 = ['01','02','03','04','05','06','07','08','09','10','11','12']
if '/' in date:
   date = date.split('/')
   date[0],date[1] = date[1],date[0]
   date ='/'.join(date)
   print(date)
else:
    date = date.replace(',','').split()
    date[0] = month1[month.index(date[0])]
    date[0],date[1] = date[1],date[0]
    date = '/'.join(date)
    print(date) 
#Works fine

