time = input('Time/AM/PM:').upper()
tw_am = ['00','01','02','03','04','05','06','07','08','09','10','11']
tw_pm = ['12','13','14','15','16','17','18','19','20','21','22','23']
tw = ['12','1','2','3','4','5','6','7','8','9','10','11']

if 'AM' in time:
  time = time.strip(' AM').lstrip('0').split(':')
  time[0] = '{}'.format(tw_am[tw.index(time[0])])
  time[1] = time[1].zfill(2)
  time = ':'.join(time)
  print(time)
else:
  time = time.strip(' PM').lstrip('0').split(':')
  time[0] = '{}'.format(tw_pm[tw.index(time[0])]) 
  time[1] = time[1].zfill(2)  
  time = ':'.join(time) 
  print(time)   
  # Works Fine 

alpha = "a b c d"