import pygame
import random
import constant

pygame.init()
gameDisplay = pygame.display.set_mode((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))

background_colour = (89, 89, 89)
snake_color = (255, 125, 64)
gameDisplay.fill(background_colour)

pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

x_vel = 10
y_vel = 10

x_fac = 0
y_fac = 0

x_pos = 10
y_pos = 300

right = pygame.K_RIGHT
left = pygame.K_LEFT
up = pygame.K_UP
down = pygame.K_DOWN

alive = True


def wall_collision():
    global x_fac
    global y_fac
    global alive
    if x_pos >= (constant.SCREEN_WIDTH-constant.SNAKE_SIZE):
        alive = False
        x_fac = 0
    if x_pos <= 0:
        alive = False
        x_fac = 0
    if y_pos >= (constant.SCREEN_HEIGHT-constant.SNAKE_SIZE):
        alive = False
        y_fac = 0
    if y_pos <= 0:
        alive = False
        y_fac = 0


RUNNING, PAUSE = 0, 1
state = RUNNING
pause_text = pygame.font.SysFont('Consolas', 32).render('Paused - Press SPACE to resume', True, pygame.color.Color('White'))
dead_text = pygame.font.SysFont('Consolas', 32).render('You died!', True, pygame.color.Color('White'))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_fac = 1
                y_fac = 0
            if event.key == left:
                x_fac = -1
                y_fac = 0
            if event.key == up:
                x_fac = 0
                y_fac = -1
            if event.key == down:
                x_fac = 0
                y_fac = 1
            if event.key == pygame.K_p:
                state = PAUSE
            if event.key == pygame.K_SPACE:
                state = RUNNING

    if alive:
        if state == RUNNING:
            wall_collision()

            x_pos = x_pos + (x_vel*x_fac)
            y_pos = y_pos + (y_vel*y_fac)

            gameDisplay.fill(background_colour)
            pygame.draw.rect(gameDisplay, snake_color, (x_pos, y_pos, constant.SNAKE_SIZE, constant.SNAKE_SIZE), 0)

        elif state == PAUSE:
            gameDisplay.blit(pause_text, (100, 100))

    else:
        gameDisplay.blit(dead_text, (100, 100))

    pygame.display.update()
    clock.tick(constant.GAME_SPEED)

    #pygame.event.pump()
