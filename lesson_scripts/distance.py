x1 = 1
y1 = 2
x2 = 4
y2 = 6

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(distance)



def calcDistance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

ourdistance  = calcDistance(1,2,4,6)

calcDistance(x1=1,y1=2,x2=4,y2=6)