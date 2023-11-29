from pygame import *
from random import randint

font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))

goal = 5

img_player = "racket.png"
img_ball = "tenis_ball.png"

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.y))

class P1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.x += self.speed

class P2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_S] and self.rect.y < win_width - 80:
            self.rect.x += self.speed
player1 = P1(img_player 5, win_height - 100, 80, 100, 10)


win_width = 700
win_height = 500
display.set_caption("Ping Pong")
window = display.set_mode((win_width, win_height))

clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        for e.type == QUIT:
            game = False
    