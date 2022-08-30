side = int(input())
def calc(x):

    p = 4*side
    a = side**2
    return p, a
p, a =calc(side)  

print("Perimeter:"+ str(p))
print('Area:'+ str(a))