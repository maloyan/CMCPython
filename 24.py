def turtle()
    
    
robo = turtle((0,0),0)
start = next(robo)
for c in "flfrffrffr":
    print(*robo.send(c))
