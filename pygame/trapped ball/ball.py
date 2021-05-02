import pygame, os, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
mainSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Seguimiento")
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 128, 0)
barreraIzq = pygame.Rect(0, 0, 50, 600)
barreraDer = pygame.Rect(750, 0, 50, 600)

#ball init
ball = pygame.image.load("ball.png")
ballRect = ball.get_rect()
paso = 50
ballServed = False
bx = 25
by = 25
ballRect.topleft = (bx, by)


while True:
    mainSurface.fill(white)
    pygame.draw.rect(mainSurface, red, barreraIzq)
    pygame.draw.rect(mainSurface, green, barreraDer)
    mainSurface.blit(ball, ballRect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_DOWN:
            if by == 425:
                ballRect.topleft = (bx, by)
            else:
                by = by + paso
                ballRect.topleft = (bx, by)
        elif event.type == KEYDOWN and event.key == K_UP:
            if by == -25:
                ballRect.topleft = (bx, by)
            else:
                by = by - paso
                ballRect.topleft = (bx, by)
        elif event.type == KEYDOWN and event.key == K_LEFT:
            if bx == 25:
                ballRect.topleft = (bx, by)
            else:
                bx = bx - paso
                ballRect.topleft = (bx, by)
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            if bx == 575:
                ballRect.topleft = (bx, by)
            else:
                bx = bx + paso
                ballRect.topleft = (bx, by)
        pygame.display.update()
        fpsClock.tick(30)
