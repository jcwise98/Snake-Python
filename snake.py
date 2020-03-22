import pygame
import constant
import snakelist
import objects
import random

alive = True

def gen_random():
    rand = random.randint(15, 585)
    rand = (rand - (rand % 15))
    return rand


def wall_collision():
    global x_fac
    global y_fac
    global alive
    if snake.head.x >= (constant.SCREEN_WIDTH - constant.SNAKE_SIZE):
        alive = False
        x_fac = 0
    if snake.head.x <= 0:
        alive = False
        x_fac = 0
    if snake.head.y >= (constant.SCREEN_HEIGHT - constant.SNAKE_SIZE):
        alive = False
        y_fac = 0
    if snake.head.y <= 0:
        alive = False
        y_fac = 0


def food_collision():
    if (snake.head.x == food.x) and (snake.head.y == food.y):
        add_snake()
        food.x = gen_random() + 10
        food.y = gen_random()


def self_collision():
    global alive
    curr = snake.head.next
    while curr is not None:
        if (snake.head.x == curr.x) and (snake.head.y == curr.y):
            alive = False
        curr = curr.next


def add_snake():
    curr = snake.head
    while curr.next is not None:
        curr = curr.next
    curr.next = snakelist.SNode(curr.xprev, curr.yprev)
    snake.length += 1


pygame.init()
gameDisplay = pygame.display.set_mode((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))

background_colour = (89, 89, 89)
snake_color = (255, 125, 64)
food_color = (255, 0, 0)
gameDisplay.fill(background_colour)

pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

x_vel = 15
y_vel = 15

x_fac = 0
y_fac = 0

snake = snakelist.SLinkedList()
snake.head = snakelist.SNode()

food = objects.FoodObj(gen_random() + 10, gen_random())

right = pygame.K_RIGHT
left = pygame.K_LEFT
up = pygame.K_UP
down = pygame.K_DOWN

RUNNING, PAUSE = 0, 1
state = RUNNING
pause_text = pygame.font.SysFont('Consolas', 32).render('Paused - Press SPACE to resume', True,
                                                        pygame.color.Color('White'))
dead_text = pygame.font.SysFont('Consolas', 32).render('You died!', True, pygame.color.Color('White'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == right:
                if (snake.length > 1) and (x_fac == -1) and (y_fac == 0):
                    pass
                else:
                    x_fac = 1
                    y_fac = 0
            if event.key == left:
                if (snake.length > 1) and (x_fac == 1) and (y_fac == 0):
                    pass
                else:
                    x_fac = -1
                    y_fac = 0
            if event.key == up:
                if (snake.length > 1) and (x_fac == 0) and (y_fac == 1):
                    pass
                else:
                    x_fac = 0
                    y_fac = -1
            if event.key == down:
                if (snake.length > 1) and (x_fac == 0) and (y_fac == -1):
                    pass
                else:
                    x_fac = 0
                    y_fac = 1
            if event.key == pygame.K_p:
                state = PAUSE
            if event.key == pygame.K_a:
                add_snake()
            if event.key == pygame.K_SPACE:
                state = RUNNING

    if alive:
        if state == RUNNING:
            wall_collision()
            food_collision()
            self_collision()

            if alive:
                snake.head.xprev = snake.head.x
                snake.head.yprev = snake.head.y
                snake.head.x += (x_vel * x_fac)
                snake.head.y += (y_vel * y_fac)

            gameDisplay.fill(background_colour)
            current = snake.head
            while current is not None:
                pygame.draw.rect(gameDisplay, snake_color,
                                 (current.x, current.y, constant.SNAKE_SIZE, constant.SNAKE_SIZE), 0)
                pygame.draw.rect(gameDisplay, background_colour,
                                 (current.x, current.y, constant.SNAKE_SIZE, constant.SNAKE_SIZE), 1)
                if current.next is not None:
                    current.next.xprev = current.next.x
                    current.next.yprev = current.next.y
                    current.next.x = current.xprev
                    current.next.y = current.yprev
                current = current.next

            pygame.draw.rect(gameDisplay, food_color,
                             (food.x, food.y, constant.SNAKE_SIZE, constant.SNAKE_SIZE), 0)
            pygame.draw.rect(gameDisplay, background_colour,
                             (food.x, food.y, constant.SNAKE_SIZE, constant.SNAKE_SIZE), 1)
        elif state == PAUSE:
            gameDisplay.blit(pause_text, (100, 100))

    else:
        gameDisplay.blit(dead_text, (100, 100))

    pygame.display.update()
    clock.tick(constant.GAME_SPEED)

    # pygame.event.pump()
