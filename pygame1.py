import pygame

pygame.init()

#CREATE SCREEN
screen = pygame.display.set_mode((800, 600))

#GAME lOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False


















