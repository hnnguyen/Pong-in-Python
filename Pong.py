__author__ = 'henrynguyen'
import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pong Pong!")

#Creating a ball and background.
back = pygame.Surface((640,480))
background = back.convert()
background.fill((0,0,0))
circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(255,255,255),(7,7),10)
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))

circlex = 307.5
circley = 232.5
speedx = 200
speedy = 200
speed_circ = 200

clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background,(0,0))
    screen.blit(circle,(circlex,circley))

# movement of circle
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0

    circlex += speedx * time_sec
    circley += speedy * time_sec

#ball collision
    if circlex < 5.:
        speedx = -speedx
    elif circlex > 635.:
        speedx = -speedx
    if circley <= 5.:
        speedy = -speedy
    elif circley >= 475:
        speedy = -speedy


    pygame.display.update()