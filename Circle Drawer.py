import pygame, math, random, sys
import ctypes
user32 = ctypes.windll.user32

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)), pygame.FULLSCREEN)
def dist(x, y, x1, y1):
    return math.sqrt(math.pow(x1-x,2)+math.pow(y1-y,2))
class circle():
    def __init__(self, center, radius):
        m=200
        self.color=(int(shade), int(shade), int(shade))
        self.color=(random.randint(0, m), random.randint(0, m), random.randint(0, m))
        self.center=center
        self.radius=radius
        self.rect=pygame.Rect(center[0]-radius, center[0]-radius, radius*2, radius*2)
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.center, int(self.radius))
    def intersectingPoint(self, x, y):
        return dist(self.center[0], self.center[1], x, y)<self.radius
    def distanceTo(self, x, y):
        return dist(self.center[0], self.center[1], x, y)-self.radius
    
circles=[]
shade=0
while 1:
    stop=False
    while not stop:
        stop=True
        center=[random.randint(0, screen.get_width()), random.randint(0, screen.get_height())]
        for c in circles:
            if c.intersectingPoint(center[0], center[1]):
                stop=False
    radii=[center[0], center[1], screen.get_width()-center[0], screen.get_height()-center[1]]
    for c in circles:
        radii.append(c.distanceTo(center[0], center[1]))
    #print(center, radii)
    circles.append(circle(center, min(radii)))
    screen.fill((0,0,0))
    shade+=.5
    for c in circles:
        c.draw(screen)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key==pygame.K_SPACE:
                circles=[]
print('end?')
        

