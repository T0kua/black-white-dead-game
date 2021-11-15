#import
import pygame
import random
import time
#var and const
width = 600
height = 460
fps = 60
white = (255,255,255)
black = (0,0,0)
color = [white,black]
score = 0
speed = 2
#sistem 
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
game = True
pygame.display.set_caption("game play ")
all_sprites = pygame.sprite.Group()
#def and function
def Score(): 
    global score
    score += 1;
    global speed
    speed += 0.1
    pygame.display.set_caption("game         score : " + str(score))
def flip() : pygame.display.flip()
#class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((120, 30))
        self.image.fill(color[1])
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2,height - 40)
    def update(self):
        self.image.fill(color[1])
        if self.rect.right > width :
            self.rect.right = width
        r = self.rect.center
        if self.rect.x < 0 :
            self.rect.left = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 5
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 5
    def r(self) : return(self.rect.x)
class Rect(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(color[1])
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0,width - 30),0)
    def update(self): 
        self.image.fill(color[1])
        self.rect.y += speed
        if self.rect.y > height:
            pygame.display.set_caption("game over")
            time.sleep(1)
            exit()
        if player.r() + 120 >= self.rect.x >= player.r() and 420 > self.rect.y > 410:
            self.rect.center = (random.randint(10,width - 10),0)
            Score()
player = Player()
rect = Rect()
all_sprites.add(rect)
all_sprites.add(player)
#cicle
while game == True :
    clock.tick(fps)
    screen.fill(color[0])
    all_sprites.update()
    all_sprites.draw(screen)
    random.shuffle(color)
    flip()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            game = False;
pygame.quit()
