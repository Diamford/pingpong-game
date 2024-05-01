from pygame import *
win_width = 600
win_heigh = 500
window = display.set_mode(
    (win_width, win_heigh)
)
class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, width, heigh):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width, heigh))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def control(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 495:
            self.rect.y += self.speed

class Player2(GameSprite):
    def control(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed

class Ball(GameSprite):
    def move(self):
        
    
display.set_caption('eeeeeeeeeeeee')
window.fill((255,255,0))
run = True
FPS = 60
clock = time.Clock()
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(FPS)
