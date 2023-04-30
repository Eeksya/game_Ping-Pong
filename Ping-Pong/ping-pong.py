from pygame import *
from random import randint
mixer.init()
font.init()


mw = display.set_mode((700,600))
display.set_caption('Ping-Pong')
BG = transform.scale(image.load('sprites/galaxy.jpg'), (700, 600))


run = True
clock = time.Clock()
move2 = ''
win1 = 0
win2 = 0


class GameSprite(sprite.Sprite):
    def __init__(self, x, y, w, h, img, speed=0):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    def update2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed


player1 = Player(20, 10, 25, 150, 'sprites/platform1.png', 10)
player2 = Player(660, 430, 25, 150, 'sprites/platform2.png', 10)


class Ball(GameSprite):
    def start(self):
        global move2
        a = randint(1, 2)
        self.rect.x = 340
        self.rect.y = 290
        if a == 1:
            self.move = 'up'
        else:
            self.move = 'down'
        a = randint(1, 2)
        if a == 1:
            move2 = 'right'
        else:
            move2 = 'left'
    def update(self):
        global move2, win1, win2

        if self.rect.y <= 0:
            self.move = 'down'
        elif self.rect.y >= 580:
            self.move = 'up'

        if self.move == 'down':
            self.rect.y += self.speed
        elif self.move == 'up':
            self.rect.y -= self.speed
        else:
            pass
        
        if move2 == 'right':
            self.rect.x += self.speed
        elif move2 == 'left':
            self.rect.x -= self.speed

        if self.rect.x <= -20:
            win1 += 1
            self.start()
        elif self.rect.x >= 720:
            win2 += 1
            self.start()



ball = Ball(340, 290, 20, 20, "sprites/ball.png", 10)
ball.start()

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if sprite.collide_rect(player1, ball):
        move2 = 'right'
    elif sprite.collide_rect(player2, ball):
        move2 = 'left'
    mw.blit(BG, (0,0))
    player1.reset()
    player1.update()
    player2.reset()
    player2.update2()
    ball.reset()
    ball.update()
    display.update()
    clock.tick(60)
