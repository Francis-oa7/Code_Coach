my_name = input()
agents = int(input())
o_names = input().split()
o_names.append(my_name)
o_names.sort()

position = o_names.index(my_name) + 1
def new_l():
 if agents >= position:
     return 20
 else:
     if agents == 1:
       return 20 *  position
     else:
         return 20*2   
print(new_l())     
# Works fine    
