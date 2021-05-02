import pygame, os, sys
from pygame.locals import *

#initilize pygame
pygame.init() #initialize PyGame
fpsClock = pygame.time.Clock() #instance of Clock
surface = pygame.display.set_mode((800,600)) #surface for background and sprites
background = pygame.Color(100,149,237) #set color

#load squirtle
squirtle = pygame.image.load("statics/squirtle.png") #w200 x h195
squirtleRect = squirtle.get_rect()
squirtlestartX = 0
squirtleStep = 3
squirtleRect = (squirtlestartX,600-195)

#load fireball
fireball = pygame.image.load("statics/pngwave.png") #100 x 100
ballRect = fireball.get_rect()
ballstartY = 200
ballSpeed = 3
ballServed = False
bx, by = (20,ballstartY)
sx, sy = (ballSpeed,ballSpeed)
ballRect.topleft = (bx,by)

##main loop##
while True:
    surface.fill(background) #clear surface with bgcolor
    surface.blit(squirtle,squirtleRect) #blit(image,position,area)
    surface.blit(fireball,ballRect)
    ##get events##
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP and event.key == K_RIGHT:
            squirtlestartX += squirtleStep
            squirtleRect = (squirtlestartX,600-195) 
        elif event.type == MOUSEBUTTONUP and not ballServed:
            ballServed = True
    ##main game logic##
    
    #ball movement
    if ballServed:
        bx += sx
        by += sy
        ballRect = (bx,by)
    #ball bounce afte wall collision
    if (by <= 0):
        by = 0
        sy *= -1
    if (by >= 600 - 100):
        by = 600 - 100
        sy *= -1  
    if (bx <= 0):
        bx = 0
        sx *= -1
    if (bx >= 800 - 100):
        bx = 800 - 100
        sx *= -1
    ##update screen##
    pygame.display.update()
    fpsClock.tick(30) #30 is the max value
