from pygame import *
from random import *

FPS = 60
Game = True
Finish = False
clock = time.Clock()
back = 'back.png'
sun = 'sun.png'
img_enemy = 'cloud.png'
coem = 'coems.png'
speed = 10
win_width = 700
win_height = 500
score = 0
goal = 100

font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN YAY!', True, (255, 255, 255))
lose = font1.render('HA HA YOU LOSER!', True, (180, 0, 0))
font2 = font.Font(None, 36)

class GameSprite(sprite.Sprite):
    def __init__(self, player_im, player_x, player_y, sixe_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_im), (sixe_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0

window = display.set_mode((700, 500))
display.set_caption('Sun fall')

background = transform.scale(
    image.load('back.png'),
    (700, 500)
)
clouds = sprite.Group()
coems = sprite.Group()

for i in range(1, 6):
    cloud = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    clouds.add(cloud)

for i in range(1, 2):
    coem = Enemy(coem, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    coems.add(coem)

window.blit(background, (0, 0))

sun = Player(sun, 5, win_height - 100, 100, 100, 10)




while Game:
    for e in event.get():
        if e.type == QUIT:
            Game = False
    
    if not Finish:
        window.blit(background,(0, 0))
        sun.update()
        clouds.update()
        coems.update()

        sun.reset()
        clouds.draw(window)
        coems.draw(window)
        
        if sprite.spritecollide(sun, clouds, False,):
            Finish = True
            window.blit(lose, (100, 200))
        
        if sprite.spritecollide(sun, coems, False,): # здесьььь!!!!!!!!!!!!
            score += 5
            coem.kill()
            coem.reset()

        if score >= goal:
            Finish = True
            window.blit(win, (150, 200))
        
        for c in clouds:
            if c.rect.y == 0:
                score += 1
                c.reset()

        text = font2.render('Счет: ' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        display.update()
    else:
        Finish = False
        score = 0
        for c in clouds:
            c.kill()
        for c in coems:
            c.kill()

        time.delay(3000)
        for i in range(1, 6):
            cloud = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            clouds.add(cloud)
        
        for i in range(1, 6):
            coem = Enemy(coem, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            coems.add(coem)

    time.delay(50)

display.update()
clock.tick(FPS)

