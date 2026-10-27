from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()


def draw_screen():
    color=(255,255,255)
    ind=0
    for i in range(225):
        x,y=ind%600,40*(ind//600)
        rect = pg.Rect(x, y, 20, 20)
        pg.draw.rect(screen, color, rect)
        ind+=40
    ind=20
    for i in range(225):
        x,y=ind%600,40*(ind//600)+20
        rect = pg.Rect(x, y, 20, 20)
        pg.draw.rect(screen, color, rect)
        ind+=40
#On dessine 450 pixels en tout

while True:
    clock.tick(1)
    for event in pg.event.get():
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_q:
                pg.QUIT()

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill((0,0,0))
    #x, y = 100, 200            # coin supérieur gauche, en pixels
    #width, height = 20, 20     # largeur et hauteur, en pixels
    #color = (255, 0, 0)        # rouge, en (R, V, B)
    draw_screen()
    pg.display.update()