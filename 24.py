def turtle(coord, direction):
    command = yield coord
    while command:
        if command == 'l':
            direction = (direction + 1) % 4
        elif command == 'r':
            direction = (direction - 1) % 4
        elif command == 'f':
            if direction == 0:
                coord = (coord[0] + 1, coord[1])
            elif direction == 1:
                coord = (coord[0], coord[1] + 1)            
            elif direction == 2:
                coord = (coord[0] - 1, coord[1])
            elif direction == 3:
                coord = (coord[0], coord[1] - 1)
        command = yield coord

#robo = turtle((0,0),0)
#start = next(robo)
#for c in "flfrffrffr":
#    print(*robo.send(c))
