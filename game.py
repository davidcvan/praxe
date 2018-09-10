import pygame, sys, os
from pygame.locals import *
world = [900,800]
pygame.init()
screen = pygame.display.set_mode((world[0], world[1]))
pygame.display.set_caption('Game')
font = pygame.font.SysFont('Arial',30)
clock = pygame.time.Clock()
games = 0
goin = False
score = 0

tr = font.render('Your score was: ' + str(score), True, (255, 255, 255))


'''
def die(score):
    screen.fill((0,0,0))
    screen.blit(tr, (0, 2000));pygame.display.update()
    screen.blit(font.render('YOU LOSED', True, (255, 255, 255)), (280, 100))
'''
screen.fill((255,255,255))
ct = font.render('Welcome', True, (0, 0, 0))
screen.blit(ct, (world[0]/10, world[1]/10))
screen.blit(font.render('How many games do you want to play?', True, (0, 80, 0)), (world[0]/10, (world[1]/10)+30))
screen.blit(font.render('Press any number', True, (0, 80, 0)), (world[0]/10, (world[1]/10)+60))


class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.images = []
        self.frame = 0
        for i in range(1, 5):


            #img2 = pygame.image.load(os.path.join('/home/jmicanek/Downloads', 'sall' + '.png')).convert()

            img.convert_alpha()
            img.set_colorkey(WHITE)


            self.images.append(img)

            self.image = self.images[0]


            self.rect = self.image.get_rect()



    def control(self,a,b):
        self.movex += a
        self.movey += b



    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey



'''
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]


        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[(self.frame//ani)]

'''


fps = 40
ani = 1
pygame.init()
main = True

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
ALPHA = (0,255,0)

player2Skin = pygame.image.load(os.path.join('/home/jmicanek/Downloads','sall.png')).convert()
backdrop = pygame.image.load(os.path.join('/home/jmicanek/Downloads','papp.png')).convert()
backdropbox = screen.get_rect()

p1 = pygame.image.load(os.path.join('/home/jmicanek/Downloads', 'papp' + '.png')).convert()
p2 = pygame.image.load(os.path.join('/home/jmicanek/Downloads', 'sall' + '.png')).convert()

player = Player(p1)
player2 = Player(p2)

player.rect.x = world[0]-120
player.rect.y = world[1]-120

player2.rect.x = 20
player2.rect.y = 20

player_list = pygame.sprite.Group()
player_list.add(player)

player_list.add(player2)
steps = 10

score1 = 0
score2 = 0

con=0
con2=0

check = True

while check == True:
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            check = False
            pygame.quit()
            sys.exit()

        elif e.type == KEYDOWN:

            if e.key == K_ESCAPE:
                sys.exit()

            if games == 0:
                if e.key == K_1:
                    games = 2
                if e.key == K_2:
                    games = 4
                if e.key == K_3:
                    games = 6
                if e.key == K_4:
                    games = 8
                if e.key == K_5:
                    games = 10
                if e.key == K_6:
                    games = 12
                if e.key == K_7:
                    games = 14
                if e.key == K_8:
                    games = 16
                if e.key == K_9:
                    games = 18


            if e.key == pygame.K_LEFT:
                player.control(-steps, 0)
                con+=1
            if e.key == pygame.K_RIGHT:
                player.control(steps, 0)
                con+=100
            if e.key == pygame.K_UP:
                player.control(0, -steps)
                con+=10
            if e.key == pygame.K_DOWN:
                player.control(0, steps)
                con+=1000


            if e.key == pygame.K_a:
                player2.control(-steps, 0)
                con2+=1
            if e.key == pygame.K_d:
                player2.control(steps, 0)
                con2+=100
            if e.key == pygame.K_w:
                player2.control(0, -steps)
                con2+=10
            if e.key == pygame.K_s:
                player2.control(0, steps)
                con2+=1000


        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                player.control(steps, 0)
                con-=1
            if e.key == pygame.K_RIGHT:
                player.control(-steps, 0)
                con-=100
            if e.key == pygame.K_UP:
                player.control(0, steps)
                con-=10
            if e.key == pygame.K_DOWN:
                player.control(0, -steps)
                con-=1000

            if e.key == pygame.K_a:
                player2.control(steps, 0)
                con2-=1
            if e.key == pygame.K_d:
                player2.control(-steps, 0)
                con2-=100
            if e.key == pygame.K_w:
                player2.control(0, steps)
                con2-=10
            if e.key == pygame.K_s:
                player2.control(0, -steps)
                con2-=1000


    if games>0:
        goin=True
    else:
        goin=False
        if score1+score2>0:
            print("Salad score: ", score1)
            print("Paprika score: ", score2)
            if score1 > score2:
                print("Salad WIN")
                score1=0
                score2=0
                screen.fill((255, 255, 255))
                screen.blit(font.render('SALAD WIN', True, (0, 80, 0)), (200, 100))
                screen.blit(font.render('Press any number to start', True, (0, 80, 0)), (200, 150))
                screen.blit(font.render('ESCAPE to end', True, (0, 80, 0)), (200, 200))
            elif score2 > score1:
                print("Paprika WIN")
                score1=0
                score2=0
                screen.fill((255, 255, 255))
                screen.blit(font.render('PAPRIKA WIN', True, (0, 80, 0)), (200, 100))
                screen.blit(font.render('Press any number to start', True, (0, 80, 0)), (200, 150))
                screen.blit(font.render('ESCAPE to end', True, (0, 80, 0)), (200, 200))
            else:
                print("DRAW")
                score1=0
                score2=0

    if goin == True:
        screen.fill((255,255,255))

        #pygame.display.update()

        #screen.blit(backdrop, (0,-1000))

        if player.rect.x > 0 and 0 < player.rect.y < world[1] and con == 1 or player.rect.x > 0 and  0 < player.rect.y < world[1]-100 and con == 11 or player.rect.x > 0 and  0 < player.rect.y < world[1]-100 and con == 1001:
            player.update()
        elif player.rect.x < world[0]-100 and 0 < player.rect.y < world[1] and con == 100 or player.rect.x < world[0]-100 and 0 < player.rect.y < world[1]-100 and con == 110 or player.rect.x < world[0]-100 and  0 < player.rect.y < world[1]-100 and con == 1100 or player.rect.x < world[0] and 0 < player.rect.y < world[1] and con == 10 or player.rect.x < world[0]-100 and 0 < player.rect.y < world[1]-100 and con == 1000:
            player.update()
        elif player.rect.y > 0 and 0 < player.rect.x < world[0]-100 and con == 10 or player.rect.y > 0 and 0 < player.rect.x < world[0]-100 and con == 11 or player.rect.y > 0 and 0 < player.rect.x < world[0]-100 and con == 110:
            player.update()
        elif player.rect.y < world[1]-100 and 0 < player.rect.x < world[0] and con == 1000 or player.rect.y < world[1]-100 and 0 < player.rect.x < world[0]-100 and con == 1001 or player.rect.y < world[1]-100 and 0 < player.rect.x < world[0]-100 and con == 1100 or player.rect.y < world[1] and 0 < player.rect.x < world[0] and con == 1 or player.rect.y < 700 and 0 < player.rect.x < world[0]-100 and con == 100:
            player.update()
        elif player.rect.x == 0 and player.rect.y == 0 and con == 100 or player.rect.x == 0 and player.rect.y == 0 and con == 1000 or player.rect.x == 0 and player.rect.y == 0 and con == 1100:
            player.update()

        if player2.rect.x > 0 and 0 < player2.rect.y < world[1] and con2 == 1 or player2.rect.x > 0 and  0 < player2.rect.y < world[1]-100 and con2 == 11 or player2.rect.x > 0 and  0 < player2.rect.y < world[1]-100 and con2 == 1001:
            player2.update()
        elif player2.rect.x < world[0]-100 and 0 < player2.rect.y < world[1] and con2 == 100 or player2.rect.x < world[0]-100 and 0 < player2.rect.y < world[1]-100 and con2 == 110 or player2.rect.x < world[0]-100 and  0 < player2.rect.y < world[1]-100 and con2 == 1100 or player2.rect.x < world[0] and 0 < player2.rect.y < world[1] and con2 == 10 or player2.rect.x < world[0]-100 and 0 < player2.rect.y < world[1]-100 and con2 == 1000:
            player2.update()
        elif player2.rect.y > 0 and 0 < player2.rect.x < world[0]-100 and con2 == 10 or player2.rect.y > 0 and 0 < player2.rect.x < world[0]-100 and con2 == 11 or player2.rect.y > 0 and 0 < player2.rect.x < world[0]-100 and con2 == 110:
            player2.update()
        elif player2.rect.y < world[1]-100 and 0 < player2.rect.x < world[0] and con2 == 1000 or player2.rect.y < world[1]-100 and 0 < player2.rect.x < world[0]-100 and con2 == 1001 or player2.rect.y < world[1]-100 and 0 < player2.rect.x < world[0]-100 and con2 == 1100 or player2.rect.y < world[1] and 0 < player2.rect.x < world[0] and con2 == 1 or player2.rect.y < world[1]-100 and 0 < player2.rect.x < world[0]-100 and con2 == 100:
            player2.update()
        elif player2.rect.x == 0 and player2.rect.y == 0 and con2 == 100 or player2.rect.x == 0 and player2.rect.y == 0 and con2 == 1000 or player2.rect.x == 0 and player2.rect.y == 0 and con2 == 1100:
            player2.update()

        if games %2==0:
            screen.blit(font.render('Salat flee!', True, (0, 80, 0)), (world[0]/4, 10))
            score1+=1
            et2 = "Salad score: " + str(score1)
            screen.blit(font.render(et2, True, (0, 80, 0)), (400, 10))
            if -85 < player.rect.x - player2.rect.x < 85 and -85 < player.rect.y - player2.rect.y < 85:
                player2.rect.x = 20
                player2.rect.y = 20
                player.rect.x = world[0]-120
                player.rect.y = world[1]-120
                print("Salad",score1)
                games -= 1

        elif games%2==1:
            screen.blit(font.render('Paprika flee!', True, (0, 80, 0)), (world[0]/4, 10))
            score2+=1
            et1 = "Paprika score: " + str(score2)
            screen.blit(font.render(et1, True, (0, 80, 0)), (400, 10))
            if -85 < player.rect.x - player2.rect.x < 85 and -85 < player.rect.y - player2.rect.y < 85:
                player2.rect.x = 20
                player2.rect.y = 20
                player.rect.x = world[0]-120
                player.rect.y = world[1]-120
                print("Paprika",score2)
                games -= 1

        else:
            if games > 0:
                goin = True
            else:
                goin = False
                print("Player 1 score: ", score1)
                print("Player 2 score: ", score2)
                if score1 > score2:
                    print("Player 1 WIN")
                elif score2 > score1:
                    print("Player 2 WIN")
                else:
                    print("DRAW")

        player_list.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


        #print("con ", con)




