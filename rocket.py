import pygame
import math

pygame.init()

sw = 800
sh = 800

rocketship = pygame.image.load('graphics/rocket.png')
pygame.display.set_caption('Rocketship')
win = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()


class Player(object):
    def __init__(self):
        self.img = rocketship
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw//2
        self.y = sh//2
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))

    def draw(self, win):
        win.blit(self.rotatedSurf, self.rotatedRect)

    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)

    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)

    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))


def redrawGameWindow():
    win.fill((30, 30, 30))
    font = pygame.font.SysFont('arial', 30)
    player.draw(win)
    pygame.display.update()

player = Player()
count = 0
run = True
while run:
    clock.tick(60)
    count += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.turnLeft()
    if keys[pygame.K_RIGHT]:
        player.turnRight()
    if keys[pygame.K_UP]:
        player.moveForward()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()
pygame.quit()
