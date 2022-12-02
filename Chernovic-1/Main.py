import pygame as pg
from random import randint

pg.init()

FPS = 30
screen = pg.display.set_mode((500, 500))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


lake = []


class Entity:
    x = 0
    y = 0
    vx = 0
    vy = 0
    ax = 0
    ay = 0
    r = 0
    color = BLACK

    def move(self):
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy
        self.ax = 0
        self.ay = 0

    def draw(self):
        pg.draw.circle(screen,self.color,(self.x,self.y),self.r)

    def observe(self):
            self.ax += (30/(self.x-self.r) + 30/(self.x+self.r - 500))
            self.ay += (30 / (self.y - self.r) + 30/(self.y + self.r - 500))



class Perch(Entity):
    def __init__(self,x,y,r,vx,vy):
        self.x = x
        self.y = y
        self.r = r
        self.vx=vx
        self.vy = vy
    color = GREEN



class Pike(Entity):
    def __init__(self,x,y,r,vx,vy):
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
    color = RED

def new_entities(N):
    for i in range(N):
        lake.append(Pike(randint(100, 400),randint(100, 400),randint(10,15),randint(-5,5),randint(-5,5)))
        lake.append(Perch(randint(100, 400),randint(100, 400),randint(5,10),randint(-5,5),randint(-5,5)))


def model_update(entities):
    for fish in lake:
        Entity.observe(fish)
        Entity.move(fish)
        Entity.draw(fish)


new_entities(10)
pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
    screen.fill(BLUE)
    model_update(lake)
    pg.display.update()

pg.quit()