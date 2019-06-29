import pygame
import random

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))

background_colour = (89, 89, 89)
gameDisplay.fill(background_colour)

pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

x_vel = 15

x_fac = 1

x_pos = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # col_1 = random.randint(0, 255)
    # col_2 = random.randint(0, 255)
    # col_3 = random.randint(0, 255)
    # print(col_3)
    if (x_pos >= 800):
        x_fac = -1
    if (x_pos <= 0):
        x_fac = 1
    x_pos = x_pos + (x_vel*x_fac)
    gameDisplay.fill(background_colour)
    pygame.draw.rect(gameDisplay, (255, 125, 64), (x_pos, 300, 50, 50), 0)
    pygame.display.update()

    msElapsed = clock.tick(30)
