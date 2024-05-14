from pygame import *
from random import randint
file = open('settings.txt', 'r')
js = int(file.readline()) 
if js == 1:
    joystick.init()
    p1js = joystick.Joystick(0)
    p2js = joystick.Joystick(1)
win_width = int(file.readline())
win_heigh = int(file.readline())
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
        self.size_x = width
        self.size_y = heigh
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def control(self):
        keys_pressed = key.get_pressed()
        if js != 1:
            if keys_pressed[K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys_pressed[K_s] and self.rect.y < win_heigh-150:
                self.rect.y += self.speed
        else:
            if p1js.get_axis(1) < -0.125 and self.rect.y > 0:
                self.rect.y -= self.speed
            if p1js.get_axis(1) > 0.125 and self.rect.y < win_heigh-150:
                self.rect.y += self.speed
        
    
    def control2(self):
        keys_pressed = key.get_pressed()
        if js != 1:
            if keys_pressed[K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys_pressed[K_DOWN] and self.rect.y < win_heigh-150:
                self.rect.y += self.speed
        else:
            if p2js.get_axis(1) < -0.125 and self.rect.y > 0:
                self.rect.y -= self.speed
            if p2js.get_axis(1) > 0.125 and self.rect.y < win_heigh-150:
                self.rect.y += self.speed


ball = GameSprite('tenis_ball.png', win_width/2, win_heigh/2, int(file.readline()), int(file.readline()), int(file.readline()))
racket1 = Player('racket1.png', 10, 10, int(file.readline()), int(file.readline()), int(file.readline()))
racket2 = Player('racket2.png', win_width-60, win_heigh-160, int(file.readline()), int(file.readline()), int(file.readline()))
finish = True

mixer.init()
mixer.music.load('music.ogg')
mixer.music.play()
pong = mixer.Sound('pong.ogg')
mixer.music.set_volume(0.3)

background = transform.scale(
    image.load('background.jpeg'),
    (win_width, win_heigh)
)    
display.set_caption(file.readline())
Icon = image.load('Tenis_ball.png')
display.set_icon(Icon)
run = True
FPS = int(file.readline())
clock = time.Clock()
speed_x = ball.speed
speed_y = ball.speed
TPS = 0
Pause = False
music_TPS = 0

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (255, 255, 255))
lose2 = font1.render('PLAYER 2 LOSE!', True, (255, 255, 255))
pause = font1.render('PAUSE', True, (255, 255, 255))
creator = font1.render('Pechenkin Vladimir', True, (255, 255, 255))
a = int(file.readline())
b = int(file.readline())
while run:
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT or keys_pressed[K_ESCAPE]:
            run = False

    if music_TPS > b:
        music_TPS = 0
        mixer.music.play()

    window.blit(background, (0, 0))
    racket1.reset()
    racket2.reset()
    if finish:
        racket1.control()
        racket2.control2()
    ball.reset()
    if finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_heigh-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) and TPS > FPS:
            TPS = 0
            speed_x *= -1
            ball.image = transform.scale(image.load('tenis_ball1.png'), (ball.size_x, ball.size_y))
            pong.play()
            if a == 1:
                i = randint(1, 2)
                if speed_x < 0:
                    speed_x *= -1
                    if i == 1:
                        speed_x += 1
                    speed_x *= -1
                else:
                    if i == 1:
                        speed_x += 1
                if speed_y < 0:
                    speed_y *= -1
                    if i == 2:
                        speed_y += 1
                    speed_y *= -1
                else:
                    if i == 2:
                        speed_y += 1  
        elif sprite.collide_rect(racket2, ball) and TPS > FPS:
            TPS = 0
            speed_x *= -1
            ball.image = transform.scale(image.load('tenis_ball2.png'), (ball.size_x, ball.size_y))
            pong.play()
            if a == 1:
                i = randint(1, 2)
                if speed_x < 0:
                    speed_x *= -1
                    if i == 1:
                        speed_x += 1
                    speed_x *= -1
                else:
                    if i == 1:
                        speed_x += 1
                if speed_y < 0:
                    speed_y *= -1
                    if i == 2:
                        speed_y += 1
                    speed_y *= -1
                else:
                    if i == 2:
                        speed_y += 1

    if ball.rect.x < -50:
        finish = False
        window.blit(lose1, (win_width/3, win_heigh/2.5))
    elif ball.rect.x > win_width:
        finish = False
        window.blit(lose2, (win_width/3, win_heigh/2.5))

    
    if keys_pressed[K_SPACE] and not finish == False:
        finish = False
        Pause = True
    elif js == 1:
        if (p1js.get_button(6) or p2js.get_button(6)) and not finish == False:
            finish = False
            Pause = True
    
    if Pause:
        window.blit(pause, (win_width/3, win_heigh/2.5)) 
        if keys_pressed[K_LSHIFT]:
            finish = True
            Pause = False
        elif js == 1:
            if (p1js.get_button(5) or p2js.get_button(5)):
                finish = True
                Pause = False
    window.blit(creator, (5, win_heigh-50))

    music_TPS += 1    
    TPS += 1
    display.update()
    clock.tick(FPS)