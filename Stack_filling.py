import PIL.Image, PIL.ImageDraw 
im = PIL.Image.open(r'Write your own path')
im = im.convert('RGB')
draw = PIL.ImageDraw.Draw(im)
x = 'write the value of x that is inside the shape'
y = 'write the value of н that is inside the shape'

stack = [x,y]
while(len(stack) > 0):
    y = stack.pop()
    x = stack.pop()
    draw.point((x, y), (255,125,125)) #you can change this values to create any color you want
    if im.getpixel((x+1, y)) == (255, 255, 255):
        stack.append(x+1)
        stack.append(y)
    if im.getpixel((x-1, y)) == (255, 255, 255):
        stack.append(x-1)
        stack.append(y)
    if im.getpixel((x, y+1)) == (255, 255, 255):
        stack.append(x)
        stack.append(y+1)
    if im.getpixel((x, y-1)) == (255, 255, 255):
        stack.append(x)
        stack.append(y-1)
    
im.save(r'Write your own path')

