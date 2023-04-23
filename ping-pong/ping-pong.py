from pygame import *
mixer.init()
font.init()


mw = display.set_mode((700,600))
display.set_caption('Ping-Pong')
BG = transform.scale(image.load('sprites/galaxy.jpg'), (700, 600))


run = True
clock = time.Clock()


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

class Ball(GameSprite):

    def update(self):
        if self.rect.y == 0:
            move = down
        elif self.rect.y == 580:
            move = up
        if self.rect.x == 0:
            move2 = right 
        elif self.rect.x == 680:
            move2 = left
        if move == down:
            self.rect.y += speed
        elif move == up:
            self.rect.y -= speed
    pass

player1 = Player(20, 10, 25, 150, 'sprites/platform1.png', 10)
player2 = Player(660, 430, 25, 150, 'sprites/platform2.png', 10)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    mw.blit(BG, (0,0))
    player1.reset()
    player1.update()
    player2.reset()
    player2.update2()
    display.update()
    clock.tick(60)




























