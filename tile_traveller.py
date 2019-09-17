print('n/N for north (up)')
print('e/E for east (right)')
print('s/S for south (down)')
print('w/W for west (left)')
print('we start at (1,1)')
x=1
y=1
E='East'
y1=input('Direction: ')
def TILE_U(x,y,y1):
    if y1==s or y1==S:
        x=x 
        y=y-y1
    elif y1==e or y1==E:
        x=x+y1
        y=y
    elif y1==w or y1==W:
        x=x-y1
        y=y
    elif y1==n or y1==N:
        x=x
        y=y+y1
    return x,y
x,y,y1=TILE_U(x,y,y1)
if x==0 or y==0:
    print("Not a valid direction!")
elif