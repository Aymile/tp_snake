from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()


def draw_board():
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


def draw_snake(snake):
    for case in snake:
        pg.draw.rect(screen, (255,0,0), pg.Rect(case[0]*20, case[1]*20, 20, 20))

def move_snake(snake,direction):
    return snake[1:] + [(snake[-1][0] + direction[0], snake[-1][1] + direction[1])]

def draw_fruit(fruit):
    pg.draw.rect(screen, (0,255,0), pg.Rect(fruit[0]*20, fruit[1]*20, 20, 20))

def eat_fruit(score,snake,fruit):
    if snake[-1]==fruit:
        fruit= (randint(0, 29), randint(0, 29))
        while fruit in snake:
            fruit= (randint(0, 29), randint(0, 29))
        return (score+1,["Emile"]+snake,fruit) #On insère n'importe quoi parce qu'on le supprime juste après
    return (score,snake,fruit)

def game_over(snake):
    return snake[-1] in snake[:-1]



direction=(1,0)
SCORE=0
SNAKE=[(10, 15),
   (11, 15),
   (12, 15),]
FRUIT= (randint(0, 29), randint(0, 29))
while FRUIT in SNAKE:
    FRUIT= (randint(0, 29), randint(0, 29))
running=1
font=pg.font.Font(None,74)





while running:
    clock.tick(6)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=0
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_q:
                running=0
            if event.key==pg.K_DOWN and not direction==(0,-1):
                direction=(0,1)
            if event.key==pg.K_UP and not direction==(0,1):
                direction=(0,-1)
            if event.key==pg.K_LEFT and not direction==(1,0):
                direction=(-1,0)
            if event.key==pg.K_RIGHT and not direction==(-1,0):
                direction=(1,0)
                        
                        
    screen.fill((0,0,0))
    draw_board()
    draw_fruit(FRUIT)
    draw_snake(SNAKE)
    SCORE,SNAKE,FRUIT=eat_fruit(SCORE,SNAKE,FRUIT)
    SNAKE=move_snake(SNAKE,direction)
    if game_over(SNAKE):
        texte=font.render("Game over",True,(255,0,0))
        screen.blit(texte,(200,200))
        pg.display.flip()
        pg.time.wait(4000)
        running=0
    pg.display.update()
