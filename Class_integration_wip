import pygame
from pygame.locals import *

# Initialize
pygame.init()
# Screen
pygame.display.set_caption("images//Spaceinvaders")
player1ship = pygame.image.load("images//spaceship.png")
player1ship = pygame.transform.rotate(player1ship,180)
player2ship = pygame.image.load("images//player2ship.png")
player2ship = pygame.transform.scale(player2ship,(200,200))
galactic_background = "images//stars.jpg"
hubble_skyfullofstars_background = "images//hubble famous image.jpg"
background = pygame.image.load(galactic_background)

pygame.display.set_icon(player1ship)

size = 800, 600 # 1366x768 is native laptop height
width, height = size
screen = pygame.display.set_mode((width, height))
# variables
FPS = 60
VELOCITY = 4

class Player:
    def __init__(self, player_x, player_y, playerychange, playerxchange, key_up, key_down, key_left, key_right, image):
        self.player_x = 200
        self.player_y = 200
        self.playerychange = 0
        self.playerxchange = 0
        self.key_left = key_left
        self.key_right = key_right
        self.key_up = key_up
        self.key_down = key_down

        ship = pygame.image.load(image)
        self.image = pygame.transform.rotate(ship, 180)


                 #value of:   w  s   a   d
player1 = Player(200,200,0,0,119,115,97,100,"images//spaceship.png")


player1_x = 200
player1_y = 200
enemyx = 200
enemyy = 200
playerxchange = 0
playerychange = 0
enemyxchange = 0
enemyychange = 0



def player1handlemovement(keys_pressed):
    global player1
    #if key w is pressed
    if keys_pressed[player1.key_up]:
        #this limits the speed at which the player can travel, if this isn't here then the player will gain 4 velocity
        #for everytime they press "w"
        if player1.playerychange == -4 or player1.playerychange < -4:
            player1.playerychange = -4
        else:
            player1.playerychange -= VELOCITY

    #this key halts movement if the key w isn't pressed down, this works as well for s because it will make both movement varaibles 0
    elif keys_pressed != keys_pressed[player1.key_up]:
        player1.playerychange = 0

    #if key s is pressed
    if keys_pressed[player1.key_down]:
        #this limits the speed at which the player can travel, if this isn't here then the player will gain 4 velocity
        #for everytime they press "w"
        if  player1.playerychange == 4 or  player1.playerychange > 4:
            player1.playerychange = 4
        else:
            player1.playerychange += VELOCITY

    #if key a is pressed
    if keys_pressed[player1.key_left]:
        #read the comment above for keys "w" and "s" this does the same but for the "a" key.
        if player1.playerxchange == -4 or player1.playerxchange < -4:
            player1.playerxchange = -4
        else:
            player1.playerxchange -= VELOCITY

    # this key halts movement if the key "a" isn't pressed down, this works as well for "d" because it will make both movement varaibles 0
    elif keys_pressed != keys_pressed[player1.key_left]:
        player1.playerxchange = 0



    #if key d is pressed
    if keys_pressed[player1.key_right]:
        # read the comment above for keys "w", "s" and "a" keys. this does the same but for the "s" key.
        if player1.playerxchange == 4 or player1.playerxchange > 4:
            player1.playerxchange = 4
        else:
            player1.playerxchange += VELOCITY

def player2handlemovement(keys_pressed):
    global enemyx, enemyy
    global enemyxchange, enemyychange

    # if key w is pressed
    if keys_pressed[1073741906]:
        # this limits the speed at which the player can travel, if this isn't here then the player will gain 4 velocity
        # for everytime they press "w"
        if enemyychange == -4 or enemyychange < -4:
            enemyychange = -4
        else:
            enemyychange -= VELOCITY

    # this key halts movement if the key w isn't pressed down, this works as well for s because it will make both movement varaibles 0
    elif keys_pressed != keys_pressed[K_UP]:
        enemyychange = 0

    # if key s is pressed
    if keys_pressed[K_DOWN]:
        # this limits the speed at which the player can travel, if this isn't here then the player will gain 4 velocity
        # for everytime they press "w"
        if enemyychange == 4 or enemyychange > 4:
            enemyychange = 4
        else:
            enemyychange += VELOCITY

    # if key a is pressed
    if keys_pressed[K_LEFT]:
        # read the comment above for keys "w" and "s" this does the same but for the "a" key.
        if enemyxchange == -4 or enemyxchange < -4:
            enemyxchange = -4
        else:
            enemyxchange -= VELOCITY

    # this key halts movement if the key "a" isn't pressed down, this works as well for "d" because it will make both movement varaibles 0
    elif keys_pressed != keys_pressed[K_LEFT]:
        enemyxchange = 0

    # if key d is pressed
    if keys_pressed[K_RIGHT]:
        # read the comment above for keys "w", "s" and "a" keys. this does the same but for the "s" key.
        if enemyxchange == 4 or enemyxchange > 4:
            enemyxchange = 4
        else:
            enemyxchange += VELOCITY

# FUNCTIONS

def playerborder():
    global player1_x, player1_y
    if player1_x >= 692:
        player1_x = 692
    elif player1_x < -19:
        player1_x = -19
    if player1_y <= -7:
        player1_y = -7
    elif player1_y >= 479:
        player1_y = 479

def enemyborder():
    global enemyx, enemyy
    if enemyx >= 692:
        enemyx = 692
    elif enemyx < -19:
        enemyx = -19
    if enemyy <= -19:
        enemyy = -19
    elif enemyy >= 479:
        enemyy = 479


def player():
    screen.blit(player1.image, (player1.player_x, player1.player_y))


def enemy():
    screen.blit(player2ship, (enemyx, enemyy))

def draw():
    screen.blit(player1.image, (player1.player_x, player1.player_y))
    screen.blit(player2ship, (enemyx, enemyy))
    pygame.display.update()


def main():
    global player, player1_x, player1_y, enemyx, enemyy, playerxchange, playerychange, enemyychange, enemyxchange
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        screen.fill((255,255,255))
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()
            player1handlemovement(keys_pressed)
            player2handlemovement(keys_pressed)
        player1.player_y += player1.playerychange
        player1.player_x += player1.playerxchange
        enemyx += enemyxchange
        enemyy += enemyychange
        playerborder()
        enemyborder()

        draw()

    pygame.quit()


main()
