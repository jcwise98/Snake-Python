import pygame
import constant
import snakelist

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

snake = snakelist.SLinkedList()
snake.head = snakelist.SNode()
# snake.head.next = snakelist.SNode(10, 300)

right = pygame.K_RIGHT
left = pygame.K_LEFT
up = pygame.K_UP
down = pygame.K_DOWN

alive = True


def wall_collision():
    global x_fac
    global y_fac
    global alive
    if snake.head.x >= (constant.SCREEN_WIDTH-constant.SNAKE_SIZE):
        alive = False
        x_fac = 0
    if snake.head.x <= 0:
        alive = False
        x_fac = 0
    if snake.head.y >= (constant.SCREEN_HEIGHT-constant.SNAKE_SIZE):
        alive = False
        y_fac = 0
    if snake.head.y <= 0:
        alive = False
        y_fac = 0


def add_snake():
    curr = snake.head
    while curr.next is not None:
        curr = curr.next
    curr.next = snakelist.SNode(curr.xprev, curr.yprev)


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
            if event.key == pygame.K_a:
                add_snake()
            if event.key == pygame.K_SPACE:
                state = RUNNING

    if alive:
        if state == RUNNING:
            wall_collision()

            snake.head.xprev = snake.head.x
            snake.head.yprev = snake.head.y
            snake.head.x += (x_vel*x_fac)
            snake.head.y += (y_vel*y_fac)

            gameDisplay.fill(background_colour)
            current = snake.head
            counter = 0
            while current is not None:
                pygame.draw.rect(gameDisplay, snake_color,
                                 (current.x, current.y, constant.SNAKE_SIZE, constant.SNAKE_SIZE), 0)
                print(counter,": [",current.x,", ",current.y,"]")
                if current.next is not None:
                    current.next.xprev = current.x
                    current.next.yprev = current.y
                    current.next.x = current.xprev
                    current.next.y = current.yprev
                current = current.next
                counter+=1

        elif state == PAUSE:
            gameDisplay.blit(pause_text, (100, 100))

    else:
        gameDisplay.blit(dead_text, (100, 100))

    pygame.display.update()
    clock.tick(constant.GAME_SPEED)

    # pygame.event.pump()
