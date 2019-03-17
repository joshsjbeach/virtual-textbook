import pygame
import time
import math
pygame.init()

def start():
    win = pygame.display.set_mode((700,700))
    win.fill((162,202,247))
    pygame.display.set_caption("Maths Textbook")
    pygame.display.update()
    UI(win)

def UI(win):
    num = 0
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            square(win,num)
            num += 20

    pygame.quit()

def square(win,num):
    pygame.draw.rect(win, (255,0,0), (num,0,20,20))
    pygame.display.update()
    return
start()
