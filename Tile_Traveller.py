###### Tile Travel

## map 3x3

def movement(movemnt_str, x, y):
    if movemnt_str == 'n':
        y += 1
    elif movemnt_str == 's':
        y -= 1
    elif movemnt_str == 'w':
        x -= 1
    elif movemnt_str == 'e':
        x += 1
    return x, y


## Tiles (movement possibilities)
Tile1_1 = '(N)orth.'
Tile1_2 = '(N)orth or (E)ast or (S)outh.'
Tile1_3 = '(E)ast or (S)outh.'
Tile2_1 = '(N)orth.'
Tile2_2 = '(S)outh or (W)est'
Tile2_3 = '(E)ast or (W)est'
Tile3_1 = "Victory!"
Tile3_2 = '(N)orth or (S)outh.'
Tile3_3 = '(S)outh or (W)est'

loc_x, loc_y = 1,1
print(Tile1_1)
move = input("Direction: ").lower()

eysteinn = 'news'
## beginning
while move in eysteinn:
    current_loc = Tile1_1
    u = movement(move, loc_x, loc_y)
    loc_x = u[0]
    loc_y = u[1]

    print(loc_x,loc_y) #Til þess að sjá staðsetningu

    ## Tiles location
    if loc_x == 1 and loc_y == 1:
        current_loc = Tile1_1
        print(Tile1_1)
    elif loc_x == 1 and loc_y == 2:
        current_loc = Tile1_2        
        print(Tile1_2)
    elif loc_x == 1 and loc_y == 3:
        current_loc = Tile1_3
        print(Tile1_3)
    elif loc_x == 2 and loc_y == 1:
        current_loc = Tile2_1
        print(Tile2_1)
    elif loc_x == 2 and loc_y == 2:
        current_loc = Tile2_2
        print(Tile2_2)
    elif loc_x == 2 and loc_y == 3:
        current_loc = Tile2_3
        print(Tile2_3)
    elif loc_x == 3 and loc_y == 2:
        current_loc = Tile3_2
        print(Tile3_2)
    elif loc_x == 3 and loc_y == 3:
        current_loc = Tile3_3
        print(Tile3_3)
    elif loc_x == 3 and loc_y == 1:
        print(Tile3_1)
        break

    move = input("Direction: ")
else:
    print("Not a valid direction!")
    #print(current_loc)
    move = input("Direction: ")

