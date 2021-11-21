import sys
 
import pygame, random
from pygame.locals import *
 
pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Particles')

particles = []

class Particle:
    def __init__(self, pos, vel, timer):
        self.pos = pos
        self.vel = vel
        self.timer = timer

fps = 60
fpsClock = pygame.time.Clock()
addMore = False
# Game loop.
while True:
    screen.fill((0, 0, 0))
    
    mx, my = pygame.mouse.get_pos()
    
    for particle in particles:
        particle.pos[0] += particle.vel[0]
        particle.pos[1] += particle.vel[1]
        particle.timer -= 0.05
        particle.vel[1] += 0.1
        pygame.draw.circle(screen, (255,255,255), [int(particle.pos[0]), int(particle.pos[1])], int(particle.timer))
        if particle.timer <= 0:
            particles.remove(particle)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            addMore = True
        elif event.type == pygame.MOUSEBUTTONUP:
            addMore = False

    if addMore:
        particles.append(Particle([mx, my], [random.randint(0, 20) / 10 - 1, 2], random.randint(4, 6)))

    pygame.display.flip()
    fpsClock.tick(fps)