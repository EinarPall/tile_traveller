###### Tile Travel

## map 3x3

def movement(movemnt_str, x, y):
    if movemnt_str == 'n':
        loc_y += 1
    elif movemnt_str == 's':
        loc_y -= 1
    elif movemnt_str == 'w':
        loc_x -= 1
    elif movemnt_str == 'e':
        loc_x += 1
    return loc_x, loc_y


## Tiles (movement possibilities)
Tile1_1 = '(N)orth.'
Tile1_2 = '(N)orth or (E)ast or (S)outh.'
Tile1_3 = '(E)ast or (S)outh.'
Tile2_1 = '(N)orth.'
Tile2_2 = '(S)outh or (W)est'
Tile2_3 = '(E)ast or (W)est'
Tile3_2 = '(N)orth or (S)outh.
Tile3_3 = '(S)outh or (W)est'


## beginning
loc_x, loc_y = 1,1
move = input("Direction: ").lower()
current_loc = Tile1_1


## Tiles location
if loc_x == 1 and loc_y == 1:
    print(Tile1_1)
elif loc_x == 1 and loc_y == 2:
    print(Tile1_2)
elif loc_x == 1 and loc_y == 3:
    print(Tile1_3)
elif loc_x == 2 and loc_y == 1:
    print(Tile2_1)
elif loc_x == 2 and loc_y == 2:
    print(Tile2_2)
elif loc_x == 2 and loc_y == 3:
    print(Tile2_3)
elif loc_x == 3 and loc_y == 2:
    print(Tile3_2)
elif loc_x == 3 and loc_y == 3:
    print(Tile3_3)




