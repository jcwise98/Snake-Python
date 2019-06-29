import pygame
import random

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))

background_colour = (0, 255, 0)
gameDisplay.fill(background_colour)

pygame.display.set_caption('Hello World')

pygame.display.flip()
running = True
while running:
    pygame.time.wait(1000)
    col_1 = random.randint(0, 255)
    col_2 = random.randint(0, 255)
    col_3 = random.randint(0, 255)
    background_colour = (col_1, col_2, col_3)
    gameDisplay.fill(background_colour)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()