floor = input('Floor:').replace('x','')

if floor.startswith("G") or floor.endswith("G") and (floor.startswith('G') and floor.endswith('G')):
    print('ALARM')
else:
    print('quiet')
       
#Works fine.