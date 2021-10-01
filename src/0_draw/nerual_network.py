class server:
    def __init__(self,x,y,**kwargs):
        self.x = x
        self.y = y

    def draw(self):
        x = self.x
        y = self.y
        # input
        x0 = -500
        x1 = -200
        for i in range(0,3):
            y0 = 200-i*200
            circle(x0,y0,50)
            for j in range(0,5):
                line(x0,200-i*200,x1,200-j*200+200,color=grey2)

        # hidden 1
        x2 = 100
        for i in range(0,5):
            circle(x1,200-i*200+200,50)
            for j in range(0,4):
                line(x1,200-i*200+200,x2,200-j*200+100,color=grey2)

        # hidden 2
        x3 = 400
        for i in range(0,4):
            y2 = 200-i*200+100
            circle(x2,y2,50)
            for j in range(0,2):
                line(x2,y2,x3,200-j*200-100)

        # output layer
        for i in range(0,2):
            circle(x3,200-i*200-100,50)


from sg import *
from phymin import *
scene(1980,1020)
pc = server(0,0)
pc.draw()
show(inline=True)
