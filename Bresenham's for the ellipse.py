import PIL.Image, PIL.ImageDraw #One of the best f***ing libraries
def circle(a, b):
    _x = 0
    _y = b
    a_sqr = a * a #Major axis
    b_sqr = b * b #Small axis
    deltafirst = 4 * b_sqr * ((_x + 1) ** 2) + a_sqr * ((2 * _y - 1) ** 2) - 4 * a_sqr * b_sqr #If the angle between normal and horizontal > 45°(1)
    deltasecond = b_sqr * ((2 * _x + 1) ** 2) + 4 * a_sqr * ((_y + 1) ** 2) - 4 * a_sqr * b_sqr #If the angle between normal and horizontal < 45°(2)
    points = set()
    while (a_sqr * (2 * _y - 1) > 2 * b_sqr * (_x + 1)): #Situation №1
        if (deltafirst < 0): #Horizontal transition
            _x+=1
            deltafirst += 4 * b_sqr * (2 * _x + 3)
            points.add((-_x,-_y))
            points.add((_x,-_y))
        else: #Diagonal transition
            _x+=1
            deltafirst = deltafirst - 8 * a_sqr * (_y - 1) + 4 * b_sqr * (2 * _x + 3)
            _y-=1
            points.add((-_x,-_y))
            points.add((_x,-_y))
    while (_y+1 != 0): #Situation №2
        if (deltasecond < 0): #Vertical transition
            _y-=1
            deltasecond += 4 * a_sqr * (2 * _y + 3)
            points.add((-_x,-_y))
            points.add((_x,-_y))
        else: #Diagonal transition
            _y-=1
            deltasecond = deltasecond - 8 * b_sqr * (_x + 1) + 4 * a_sqr * (2 * _y + 3)
            _x+=1
            points.add((-_x,-_y))
            points.add((_x,-_y))
    return points


size = 900
a=400
b=330
rangediff = a - a//2
circle_graph = PIL.Image.new("RGB", (size, size), (0,0,0))
draw = PIL.ImageDraw.Draw(circle_graph)
p = circle(a, b) # print the point coords
print (p)

for point in p: 
    draw.point((size/2+point[0],size/2+point[1]),(255,255,255))
p = circle(a/2,b/2)

for point in p:
    draw.point((size/2+point[0],size/2+point[1]),(255,255,255))
    
for point in range(rangediff):
    draw.point((size/2+a//2+point,size/2),(255,255,255))
    draw.point((size/2-a//2-point,size/2),(255,255,255))
circle_graph.show()

