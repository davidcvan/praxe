import pygame
import sys
import random
pygame.init()
WIDTH = 1000
HEIGHT = 1000
pygame.mixer.music.load("Angry Birds Theme Song HD.mp3")
pygame.mixer.music.play(-1)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
Display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("jeba")
clock = pygame.time.Clock()
x = (WIDTH * 0.45)
y = 980
ball_x = random.randrange(10, WIDTH - 30)
ball_y = 30
score = 0


def ball():
    pygame.draw.circle(Display, red,(ball_x,ball_y), 20, 0)
    clock.tick(60)

def platform(x,y):
    object = pygame.draw.rect(Display, blue,(x,y,150,20))


x_change = 0
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -13
            elif event.key == pygame.K_RIGHT:
                x_change = 13

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    x += x_change

    Display.fill(white)
    ball()
    ball_y+=15
    if ball_y > HEIGHT+20:
        ball_x = random.randrange(10, WIDTH - 30)
        ball()
        ball_y = 30
        ball_y += 15
    platform(x, y)
    if x > WIDTH-150 or x < 0:
        x_change = 0
    if ball_y > 1000 and ball_y < 1020 and ball_x >= x and ball_x <= x+150:
        score += 1



    elif ball_y > 1000 and ball_y < 1020:
        if ball_x < x or ball_x >x+150:
            play = False
    Display.blit(pygame.font.SysFont('Arial', 30).render('Score: ' + str(score), True, (0, 0, 0)), (200, 200))
    pygame.display.update()
    clock.tick(60)