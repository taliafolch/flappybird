import pygame, random, sys
from pygame.locals import *
from platforms import Platform
from bird import Bird


pygame.init()
screen_info = pygame.display.Info()

size =(width, height) = (int(screen_info.current_w * 0.5), int(screen_info.current_w * 0.5))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0,0,0)
background = pygame.image.load('background.jpeg')
background = pygame.transform.scale(background, (width,height))


#set up game vars
platforms = pygame.sprite.Group()
startPos = (width/8, height/2)
Player = Bird(startPos)
gapSize = 200
Ticks = 0
loopCount = 70
score = 0

def lose():
    font = pygame.font.SysFont(None, 70)
    text = font.render("Bubye", True, (244,194,194))
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/2)
    while True:
        clock.tick(60)
        screen.fill(color)
        screen.blit(text, text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    platforms.empty()
                    Player.reset(startPos)
                    return


def main():
    global Ticks, loopCount
    while True:
        clock.tick(60)
        if loopCount % 90 == 0:
            toppos = random.randint(0, height//2) - 400
            platforms.add(Platform((width + 100, toppos + gapSize + 800)))
            platforms.add(Platform((width + 100, toppos), True))
            Ticks = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    Player.speed[1] = -10
        screen.fill(color)
        Player.update()
        platforms.update()
        gets_hit = pygame.sprite.spritecollide(Player, platforms, False) \
            or Player.rect.center[1] > height or Player.rect.center[1] < 15
        screen.blit(background, [0, 0])
        platforms.draw(screen)
        screen.blit(Player.image, Player.rect)
        pygame.display.flip()
        loopCount += 1

        if gets_hit:
            lose()


if __name__ == '__main__':
    main()