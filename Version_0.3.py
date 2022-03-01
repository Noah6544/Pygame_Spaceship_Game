import pygame
from pygame.locals import *
import random

# Initialize
pygame.init()


#Loading Images
spaceship_it = pygame.transform.rotate(pygame.image.load("images//spaceship_it_2.png"),180) #loads in the ship of the person who's "it"
player1ship = pygame.transform.rotate(pygame.image.load("images//spaceship.png"),180) # lods in the ship of the person who isn't it
player1ship_small = pygame.transform.scale(player1ship,(100,100))
spaceship_it_small = pygame.transform.scale(spaceship_it,(100,100))
player2ship = pygame.image.load("images//player2ship.png")
player2ship = pygame.transform.scale(player2ship,(200,200))
galactic_background = "images//stars.jpg"
hubble_skyfullofstars_background = "images//hubble famous image.jpg"
background = pygame.transform.scale(pygame.image.load(galactic_background),(1920,1279))


# variables
FPS = 60
VELOCITY = 8
VELOCITY_it = 7.5
###CLASSES
class Player:
    def __init__(self, x, y, playerychange, playerxchange, key_up, key_down, key_left, key_right, image,it_image, is_it):
        self.x = x
        self.y = y
        self.playerychange = 0
        self.playerxchange = 2
        self.key_left = key_left
        self.key_right = key_right
        self.key_up = key_up
        self.key_down = key_down
        #ship = pygame.image.load(image)
        self.image = image
        self.it_image = spaceship_it #this is the image it will switch to when tagged, helps show which player is it.
        #hitboxes are pygame rectangle objects
        self.wing_hitbox_large = pygame.Rect(self.x + 18, self.y + 45, 90, 35) # values are guessed and checked to fit well
        self.body_hitbox_large = pygame.Rect(self.x + 45, self.y + 5, 35, 115) # values are guessed and checked to fit well
        self.is_it = is_it # a simple boolean to check if you're it (True) or not it (False)


#handels hitboxes creation for player, and handles drawing image
    def draw_player_small(self, win):
        #creates a hitbox area for the wing of player 1. the numbers were guessed and checked until they were accurate
        self.wing_hitbox_small = pygame.Rect(self.x + 16, self.y + 35, 69,28)
        self.body_hitbox_small =  pygame.Rect(self.x + 37, self.y + 6, 25, 90)
        win.blit(self.image, (self.x, self.y))

    def draw_player_large(self,win):
        self.wing_hitbox = pygame.Rect(self.x + 18, self.y + 45, 90, 35)
        self.body_hitbox = pygame.Rect(self.x + 52, self.y + 5, 25, 115)
        win.blit(self.image, (self.x, self.y))

    def border_small(self):
        if self.x >= 692:
            self.x = 692
        elif self.x < -19:
            self.x = -19
        if self.y <= -7:
            self.y = -7
        elif self.y >= 479:
            self.y = 479
            #value of:   w  s   a   d

    def border_large(self):
        if self.x >= 1259:
            self.x = 1259
        elif self.x < -19:
            self.x = -19
        if self.y <= -7:
            self.y = -7
        elif self.y >= 645:
            self.y = 645


    def tagged(self):
        if self.is_it == True:
            self.is_it = False
            self.image = spaceship_it
        elif self.is_it == False:
            self.is_it = True
            self.image = player1ship

    def dice_roll():
        dice_roll = random.randint(0, 100)
        if dice_roll > 50:
            player1.is_it = True
            player2.is_it = False
        else:
            player2.is_it = True
            player1.is_it = False

    def collide_large_screen():
        # this if statements checks if the players hitboxes have collided with pygame.Rect.colliderect for each case
        # (body to body, wing to wing, wing to body)
        if pygame.Rect.colliderect(player1.wing_hitbox,player2.wing_hitbox)\
                or pygame.Rect.colliderect(player1.body_hitbox,player2.wing_hitbox)\
                or pygame.Rect.colliderect(player1.wing_hitbox, player2.body_hitbox)\
                or pygame.Rect.colliderect(player1.body_hitbox, player2.body_hitbox):
            player1.collide()
            player2.collide()

    def collide_small_screen():
        if pygame.Rect.colliderect(player1.wing_hitbox_small,player2.wing_hitbox_small)\
                or pygame.Rect.colliderect(player1.body_hitbox_small,player2.wing_hitbox_small)\
                or pygame.Rect.colliderect(player1.wing_hitbox_small, player2.body_hitbox_small)\
                or pygame.Rect.colliderect(player1.body_hitbox_small, player2.body_hitbox_small):
            player1.collide()
            player2.collide()


class wasd_player(Player):
    def __init__(self, x, y, playerychange, playerxchange, key_up, key_down, key_left, key_right, image,it_image,is_it):
        super().__init__(x, y, playerychange, playerxchange, key_up, key_down, key_left, key_right, image, it_image, is_it)
        #integrated the new inheritence class was a ton easier than i thought it was going to be.
        #super function is a life-saver, just the other day i was looking at it thinking I wasn't going to use
        #it until im wayy more experiened, but wow.

    def wasd_handlemovement(self, keys_pressed):

        if self.is_it == False:
            VELOCITY = VELOCITY_it
        elif self.is_it == True:
            VELOCITY = 8 #doing 8 instead of VELOCITY because the VELOCITY variable is subject to change and this will reset it every tag
        # if key w is pressed
        if keys_pressed[self.key_up]:
            # this limits the speed at which the player can travel, if this isn't here then the player will gain 4 velocity
            # for everytime they press "w"
            if self.playerychange == -abs(VELOCITY) or self.playerychange < -abs(VELOCITY):
                self.playerychange = -abs(VELOCITY)
            else:
                self.playerychange -= VELOCITY

        # this key halts movement if the key w isn't pressed down, this works as well for s because it will make both movement varaibles 0
        elif keys_pressed != keys_pressed[self.key_up]:
            player1.playerychange = 0

        # if key s is pressed
        if keys_pressed[self.key_down]:
            # this limits the speed at which the player can travel, if this isn't here then the player will gain 4 velocity
            # for everytime they press "w
            if self.playerychange == VELOCITY or self.playerychange > VELOCITY:
                self.playerychange = VELOCITY
            else:
                self.playerychange += VELOCITY

        # if key a is pressed
        if keys_pressed[self.key_left]:
            # read the comment above for keys "w" and "s" this does the same but for the "a" key.
            if self.playerxchange == -abs(VELOCITY) or self.playerxchange < -abs(VELOCITY):
                self.playerxchange = -abs(VELOCITY)
            else:
                self.playerxchange -= VELOCITY

        # this key halts movement if the key "a" isn't pressed down, this works as well for "d" because it will make both movement varaibles 0
        elif keys_pressed != keys_pressed[self.key_left]:
            self.playerxchange = 0

        # if key d is pressed
        if keys_pressed[self.key_right]:
            # read the comment above for keys "w", "s" and "a" keys. this does the same but for the "s" key.
            if self.playerxchange == VELOCITY or self.playerxchange > VELOCITY:
                self.playerxchange = VELOCITY
            else:
                self.playerxchange += VELOCITY

    def collide(self):
        self.tagged()
        self.x, self.y = 936, 300


class arrow_key_player(Player):
    def __init__(self, x, y, playerychange, playerxchange, key_up, key_down, key_left, key_right, image, it_image,is_it):
        super().__init__(x, y, playerychange, playerxchange, key_up, key_down, key_left, key_right, image,it_image, is_it)

    def arrow_key_handlemovement(self, keys_pressed):
        # if key w is pressed
        if self.is_it == False:
            VELOCITY = VELOCITY_it
        elif self.is_it == True:
            VELOCITY = 8 #doing 8 instead of VELOCITY because the VELOCITY variable is subject to change and this will reset it every tag
        if keys_pressed[1073741906]:
            # this limits the speed at which the player can travel, if this isn't here then the player will gain 4 velocity
            # for everytime they press "w"
            if self.playerychange == -abs(VELOCITY) or self.playerychange < -abs(VELOCITY):
                self.playerychange = -abs(VELOCITY)
            else:
                self.playerychange -= VELOCITY

        # this key halts movement if the key w isn't pressed down, this works as well for s because it will make both movement varaibles 0
        elif keys_pressed != keys_pressed[K_UP]:
            self.playerychange = 0

        # if key s is pressed
        if keys_pressed[K_DOWN]:
            # this limits the speed at which the player can travel, if this isn't here then the player will gain 4 velocity
            # for everytime they press "w"
            if self.playerychange == VELOCITY or self.playerychange > VELOCITY:
                self.playerychange = VELOCITY
            else:
                self.playerychange += VELOCITY

        # if key a is pressed
        if keys_pressed[K_LEFT]:
            # read the comment above for keys "w" and "s" this does the same but for the "a" key.
            if self.playerxchange == -abs(VELOCITY) or self.playerxchange < -abs(VELOCITY):
                self.playerxchange = -abs(VELOCITY)
            else:
                self.playerxchange -= VELOCITY

        # this key halts movement if the key "a" isn't pressed down, this works as well for "d" because it will make both movement varaibles 0
        elif keys_pressed != keys_pressed[K_LEFT]:
            self.playerxchange = 0

        # if key d is pressed
        if keys_pressed[K_RIGHT]:
            # read the comment above for keys "w", "s" and "a" keys. this does the same but for the "s" key.
            if self.playerxchange == 4 or self.playerxchange > 4:
                self.playerxchange = 4
            else:
                self.playerxchange += VELOCITY

    def collide(self):
        self.tagged()
        self.x, self.y = 200, 300

class Display():
    def __init__(self, size):
        self.size = size
        self.width,self.height = size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.is_large = False

        if self.size == (800,600):
            self.is_large = False # False mean small
        elif self.size == (1366, 768):
            self.is_large = True #True means large

    def display(self):
        pygame.display.set_mode((self.width, self.height))

    def blit(self,background,location):
        pygame.display.set_mode((self.width,self.height)).blit(background,(location))

    def draw_large(self):
        player1.draw_player_large(self.screen)
        player2.draw_player_large(self.screen)
        pygame.display.update()

    def draw_small(self):
        player1.draw_player_small(self.screen)
        player2.draw_player_small(self.screen)

player1 = wasd_player(936,300,0,0,119,115,97,100,player1ship,spaceship_it,True)
player2 = arrow_key_player(200,300,0,0,119,115,97,100,player1ship,spaceship_it,False)

# FUNCTIONS
def menu():
    screen_boolean = "large" #input(" Large or small screen ") #Small is false, true is large
    if screen_boolean == "small":
        # Screen
        pygame.display.set_caption("TAG MINIGAME")
        size = 800, 600  # 1366x768 is native laptop height
        return size
    elif screen_boolean == "large":
        # Screen
        pygame.display.set_caption("TAG MINIGAME")
        size = 1366, 768  # 1366x768 is native laptop height
        return size

def main():
    global player1, player2, size
    screen = Display(menu())
    screen.display()
    running = True
    clock = pygame.time.Clock()
    player1.tagged() # initially will decide who is it with the dice_roll variable to make one person it.
    player2.tagged()
    while running:
        clock.tick(FPS)
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if you press on the exit in the top right then it will stop the program
                running = False
        keys_pressed = pygame.key.get_pressed()
        player1.wasd_handlemovement(keys_pressed)
        player2.arrow_key_handlemovement(keys_pressed)
        player1.y += player1.playerychange
        player1.x += player1.playerxchange
        player2.x += player2.playerxchange
        player2.y += player2.playerychange
        if screen.is_large == True:
            player1.border_large()
            player2.border_large()
            screen.draw_large()
            Player.collide_large_screen()
        elif screen.is_large == False:
            player1.border_small()
            player2.border_small()
            screen.draw_small()
            Player.collide_small_screen()

    pygame.quit()

Player.dice_roll()
main()
