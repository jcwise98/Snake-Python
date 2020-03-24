import pygame
import constant
import snakelist
import objects
import random


def gen_random():
    rand = random.randint(15, 585)
    rand = (rand - (rand % 15))
    return rand


def wall_collision():
    global x_fac
    global y_fac
    global alive
    if snake.head.x > (constant.SCREEN_WIDTH - constant.SNAKE_SIZE):
        alive = False
        # pygame.mixer.Sound.play(hit_sound)
        x_fac = 0
    if snake.head.x < 0:
        alive = False
        # pygame.mixer.Sound.play(hit_sound)
        x_fac = 0
    if snake.head.y > (constant.SCREEN_HEIGHT - constant.SNAKE_SIZE):
        alive = False
        # pygame.mixer.Sound.play(hit_sound)
        y_fac = 0
    if snake.head.y < constant.SCOREBOARD:
        alive = False
        # pygame.mixer.Sound.play(hit_sound)
        y_fac = 0


def food_collision():
    global gameScore
    if (snake.head.x == food.x) and (snake.head.y == food.y):
        add_snake()
        pygame.mixer.Sound.play(eat_sound)
        gameScore += 100
        food.x = gen_random()
        food.y = gen_random() + constant.SCOREBOARD


def self_collision():
    global alive
    curr = snake.head.next
    while curr is not None:
        if (snake.head.x == curr.x) and (snake.head.y == curr.y):
            alive = False
        curr = curr.next


def add_snake():
    global gameSpeed
    curr = snake.head
    while curr.next is not None:
        curr = curr.next
    curr.next = snakelist.SNode(curr.xprev, curr.yprev)
    snake.length += 1
    gameSpeed += 1


pygame.init()
gameDisplay = pygame.display.set_mode((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))

x_vel = 15
y_vel = 15

eat_sound = pygame.mixer.Sound("sfx/eat.wav")
# hit_sound = pygame.mixer.Sound("hit.wav")
lose_sound = pygame.mixer.Sound("sfx/lose.wav")

background_colour = (89, 89, 89)
snake_color = (255, 125, 64)
food_color = (255, 250, 205)
gameDisplay.fill(background_colour)
pygame.draw.rect(gameDisplay, pygame.color.Color('Black'),
                 (0, 0, constant.SCREEN_WIDTH, constant.SCOREBOARD), 0)

pause_text = pygame.font.SysFont(constant.GAME_TEXT, constant.TEXT_SIZE).render('Paused - Press SPACE to resume', True,
                                                                                pygame.color.Color('White'))
dead_text = pygame.font.SysFont(constant.GAME_TEXT, constant.TEXT_SIZE).render('You died! Press R to restart', True,
                                                                               pygame.color.Color('White'))

pygame.display.set_caption('Snake')
while True:
    alive = True
    death = 0
    gameScore = 0
    gameSpeed = constant.GAME_SPEED
    clock = pygame.time.Clock()

    x_fac = 0
    y_fac = 0

    snake = snakelist.SLinkedList()
    snake.head = snakelist.SNode(gen_random())

    food = objects.FoodObj(gen_random(), gen_random() + constant.SCOREBOARD)

    right = pygame.K_RIGHT
    left = pygame.K_LEFT
    up = pygame.K_UP
    down = pygame.K_DOWN

    RUNNING, PAUSE = 0, 1
    state = RUNNING

    restart = True
    scoreDec = 11
    while restart:
        score_text = pygame.font.SysFont('Consolas', constant.TEXT_SIZE - 10).render(('Score: ' + str(gameScore)), True,
                                                                                     pygame.color.Color('White'))
        segment_text = pygame.font.SysFont('Consolas', constant.TEXT_SIZE - 10).render(('Segments: ' + str(snake.length)), True,
                                                                                     pygame.color.Color('White'))

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
                    snake.head.x = gen_random()
                    snake.head.y = gen_random() + constant.SCOREBOARD
                if event.key == pygame.K_SPACE:
                    state = RUNNING
                if alive is False:
                    if event.key == pygame.K_r:
                        restart = False

        if alive:
            if state == RUNNING:
                wall_collision()
                food_collision()
                self_collision()

                if alive:
                    scoreDec += 1
                    if gameScore > 0 and (scoreDec % 20 == 0):
                        gameScore -= 10
                    snake.head.xprev = snake.head.x
                    snake.head.yprev = snake.head.y
                    snake.head.x += (x_vel * x_fac)
                    snake.head.y += (y_vel * y_fac)

                gameDisplay.fill(background_colour)
                pygame.draw.rect(gameDisplay, pygame.color.Color('Black'),
                                 (0, 0, constant.SCREEN_WIDTH, constant.SCOREBOARD), 0)
                pygame.draw.rect(gameDisplay, pygame.color.Color('White'),
                                 (0, 0, constant.SCREEN_WIDTH, constant.SCOREBOARD), 1)
                gameDisplay.blit(score_text,
                                 score_text.get_rect(center=(constant.SCREEN_WIDTH / 6, constant.SCOREBOARD / 2)))
                gameDisplay.blit(segment_text,
                                 segment_text.get_rect(center=(constant.SCREEN_WIDTH / 1.25, constant.SCOREBOARD / 2)))
                if alive:
                    current = snake.head
                else:
                    current = snake.head.next
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
                gameDisplay.blit(pause_text,
                                 pause_text.get_rect(center=(constant.SCREEN_WIDTH / 2, constant.SCREEN_HEIGHT / 2)))

        else:
            if death == 0:
                pygame.time.delay(500)
                pygame.mixer.Sound.play(lose_sound)
                death = 1
            gameDisplay.blit(dead_text,
                             dead_text.get_rect(center=(constant.SCREEN_WIDTH / 2, constant.SCREEN_HEIGHT / 2)))

        pygame.display.update()
        clock.tick(gameSpeed)

        # pygame.event.pump()
    restart = True
