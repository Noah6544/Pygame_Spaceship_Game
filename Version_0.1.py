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
rect = pygame.Rect(500, 200, 90, 30)
FPS = 60
VELOCITY = 4

class Player:
    def __init__(self, x, y, playerychange, playerxchange, key_up, key_down, key_left, key_right, image):
        self.x = x
        self.y = y
        self.playerychange = 0
        self.playerxchange = 0
        self.key_left = key_left
        self.key_right = key_right
        self.key_up = key_up
        self.key_down = key_down
        ship = pygame.image.load(image)
        self.image = pygame.transform.rotate(ship, 180)
        self.wing_hitbox = pygame.Rect(self.x + 18, self.y + 45, 90, 35) # values are guessed and checked to fit well
        self.body_hitbox = pygame.Rect(self.x + 45, self.y + 5, 35, 115) # values are guessed and checked to fit well


#handels hitboxes creation for player, and handles drawing image
    def draw_player(self, win):
        #creats a hitbox area for the wing of player 1. the numbers were guessed and checked until they were accurate
        self.wing_hitbox = pygame.Rect(self.x + 18, self.y + 45, 90, 35)
        self.body_hitbox = pygame.Rect(self.x + 45, self.y + 5, 35, 115)

        win.blit(self.image, (self.x, self.y))



    def border(self):
        if self.x >= 692:
            self.x = 692
        elif self.x < -19:
            self.x = -19
        if self.y <= -7:
            self.y = -7
        elif self.y >= 479:
            self.y = 479
            #value of:   w  s   a   d

class wasd_player(Player):
    def __init__(self, x, y, playerychange, playerxchange, key_up, key_down, key_left, key_right, image):
        super().__init__(x, y, playerychange, playerxchange, key_up, key_down, key_left, key_right, image)
        #integrated the new inheritence class was a ton easier than i thought it was going to be.
        #super function is a life-saver, just the other day i was looking at it thinking I wasn't going to use
        #it until im wayy more experiened, but wow.

    def collide(self):
        self.x, self.y = 200, 200
        print("HIT!")

class arrow_key_player(Player):
    def __init__(self, x, y, playerychange, playerxchange, key_up, key_down, key_left, key_right, image):
        super().__init__(x, y, playerychange, playerxchange, key_up, key_down, key_left, key_right, image)

    def collide(self):
        self.x, self.y = 400, 200
        print("BEGIN")

player1 = wasd_player(400,200,0,0,119,115,97,100,"images//spaceship.png")
player2 = arrow_key_player(600,200,0,0,119,115,97,100,"images//spaceship.png")

enemyx = 200
enemyy = 200
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

def draw():
    global rect
    #screen.blit(player2ship, (enemyx, enemyy))
    player1.draw_player(screen)
    player2.draw_player(screen)
    pygame.display.update()

def main():
    global player1, player2, rect
    global enemyx, enemyy, enemyychange, enemyxchange
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if you press on the exit in the top right then it will stop the program
                running = False
        keys_pressed = pygame.key.get_pressed()
        player1handlemovement(keys_pressed)
        player2handlemovement(keys_pressed)
        player1.y += player1.playerychange
        player1.x += player1.playerxchange
        player2.x += enemyxchange
        player2.y += enemyychange
        player1.border()
        player2.border()
        #this if statements checks if the players hitboxes have collided with pygame.Rect.colliderect for each case
        #(body to body, wing to wing, wing to body)
        if pygame.Rect.colliderect(player1.wing_hitbox,player2.wing_hitbox)\
                or pygame.Rect.colliderect(player1.body_hitbox,player2.wing_hitbox)\
                or pygame.Rect.colliderect(player1.wing_hitbox, player2.body_hitbox)\
                or pygame.Rect.colliderect(player1.body_hitbox, player2.body_hitbox):
            player1.collide()
            player2.collide()
        draw()

    pygame.quit()


main()
