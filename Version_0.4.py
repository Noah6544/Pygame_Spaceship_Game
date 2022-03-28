import pygame
from pygame.locals import *
import random

# Initialize
pygame.init()


#Loading Images
background = pygame.transform.scale(pygame.image.load("images//stars.jpg"),(1920,1279))

##LARGE IMAGES
spaceship_it = pygame.transform.rotate(pygame.image.load("images//spaceship_it_2.png"),180) #loads in the ship of the person who's "it"
player1ship = pygame.transform.rotate(pygame.image.load("images//spaceship.png"),180) # lods in the ship of the person who isn't it

#SMALL IMAGES
player1ship_small = pygame.transform.scale(player1ship,(100,100))
spaceship_it_small = pygame.transform.scale(spaceship_it,(100,100))

#UNUSED
player2ship = pygame.image.load("images//player2ship.png")
player2ship = pygame.transform.scale(player2ship,(200,200))
galactic_background = "images//stars.jpg"
hubble_skyfullofstars_background = "images//hubble famous image.jpg"
plain_background = ((231,233,206))
plain_background_2 = ((244,227,204))


# variables
FPS = 60
CONSTANT_VELOCITY = 15
VELOCITY = 15
VELOCITY_it = 9 #Values of 5 isn't too bad, lets the "it" player try to slowly box the other player in to make the tag
                #24while still alowing the other player a chance to escape, will continue playing around with the value
                # for perfect balance
###CLASSES
class Player:
    def __init__(self, x, y,playerxchange,playerychange,key_up, key_down, key_left, key_right, not_it_image,it_image,is_it):
        self.x = x
        self.y = y
        self.playerychange = 0
        self.playerxchange = 0
        self.key_left = key_left
        self.key_right = key_right
        self.key_up = key_up
        self.key_down = key_down
        #ship = pygame.image.load(image)
        self.not_it_image = not_it_image

        self.image = not_it_image
        self.it_image = it_image #this is the image it will switch to when tagged, helps show which player is it.
        self.image_small = pygame.transform.scale(self.image,(100,100))
        self.it_image_small = pygame.transform.scale(spaceship_it,(100,100))
        #hitboxes are pygame rectangle objects
        self.wing_hitbox_large = pygame.Rect(self.x + 18, self.y + 45, 90, 35) # values are guessed and checked to fit well
        self.body_hitbox_large = pygame.Rect(self.x + 45, self.y + 5, 35, 115) # values are guessed and checked to fit well
        self.wing_hitbox_small = pygame.Rect(self.x + 16, self.y + 35, 69, 28)
        self.body_hitbox_small = pygame.Rect(self.x + 37, self.y + 6, 25, 90)
        self.is_it = is_it # a simple boolean to check if you're it (True) or not it (False)
        self.tag_score = 0



#handels hitboxes creation for player, and handles drawing image
    def draw_player_small(self, win):

        #creates a hitbox area for the wing of player 1. the numbers were guessed and checked until they were accurate
        self.wing_hitbox_small = pygame.Rect(self.x + 16, self.y + 35, 69,28)
        self.body_hitbox_small = pygame.Rect(self.x + 37, self.y + 6, 25, 90)
        win.blit(self.image_small, (self.x, self.y))

    def draw_player_large(self,win):
        self.wing_hitbox_large = pygame.Rect(self.x + 18, self.y + 45, 90, 35)
        self.body_hitbox_large = pygame.Rect(self.x + 52, self.y + 5, 25, 115)
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

    def set_initial_player_it_image(self): #this was made because the tagged() functions messes with the scoreboard system, as it will change the player's it status
        #this fucntions fixes this by not changing the players it status and is only run once at the top of the loop.
        if self.is_it == True:
            self.image = self.it_image
        elif self.is_it == False:
            self.image = self.not_it_image


    def tagged(self):
        if self.is_it == True:
            self.is_it = False
            self.image = self.not_it_image

            return False
        elif self.is_it == False:
            self.is_it = True
            self.image = self.it_image
            return True

    def collide_large_screen(player1,player2):
        # this if statements checks if the players hitboxes have collided with pygame.Rect.colliderect for each case
        # (body to body, wing to wing, wing to body)
        if pygame.Rect.colliderect(player1.wing_hitbox_large,player2.wing_hitbox_large)\
                or pygame.Rect.colliderect(player1.body_hitbox_large,player2.wing_hitbox_large)\
                or pygame.Rect.colliderect(player1.wing_hitbox_large, player2.body_hitbox_large)\
                or pygame.Rect.colliderect(player1.body_hitbox_large, player2.body_hitbox_large):
            player1.collide()
            player2.collide()


    def collide_small_screen(player1,player2):
        if pygame.Rect.colliderect(player1.wing_hitbox_small,player2.wing_hitbox_small)\
                or pygame.Rect.colliderect(player1.body_hitbox_small,player2.wing_hitbox_small)\
                or pygame.Rect.colliderect(player1.wing_hitbox_small, player2.body_hitbox_small)\
                or pygame.Rect.colliderect(player1.body_hitbox_small, player2.body_hitbox_small):
            player1.collide()
            player2.collide()



class wasd_player(Player):
    def __init__(self, x, y, playerxchange,playerychange,key_up, key_down, key_left, key_right, image,it_image,is_it):
        super().__init__(x, y,playerxchange,playerychange, key_up, key_down, key_left, key_right, image, it_image,is_it)



    def wasd_handlemovement(self, keys_pressed):
        if self.is_it == False:
            VELOCITY = CONSTANT_VELOCITY
        elif self.is_it == True:
            VELOCITY = VELOCITY_it
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
            self.playerychange = 0

        # if key s/down is pressed
        if keys_pressed[self.key_down]:
            if self.playerychange == VELOCITY or self.playerychange > VELOCITY:
                self.playerychange = VELOCITY
            else:
                self.playerychange += VELOCITY

        # if key a/left is pressed
        if keys_pressed[pygame.K_a]:
            # read the comment above for keys "w" and "s" this does the same but for the "a" key.
            if self.playerxchange == -abs(VELOCITY) or self.playerxchange < -abs(VELOCITY):
                self.playerchange = -abs(VELOCITY)
            else:
                self.playerxchange -= VELOCITY

        # this key halts movement if the key "a" isn't pressed down, this works as well for "d" because it will make both movement varaibles 0
        elif keys_pressed != keys_pressed[self.key_left]:
            self.playerxchange = 0

        # if key d/right is pressed
        if keys_pressed[self.key_right]:
            # read the comment above for keys "w", "s" and "a" keys. this does the same but for the "s" key.
            if self.playerxchange == VELOCITY or self.playerxchange > VELOCITY:
                self.playerxchange = VELOCITY
            else:
                self.playerxchange += VELOCITY

    def collide(self):
        if self.is_it:
            self.tag_score += 1
        else:
            pass

        self.tagged()
        self.x, self.y = 200, 300
        pygame.time.delay(500) # only one function needs this, not both, because it will delay the entire game.

class arrow_key_player(Player):
    def __init__(self, x, y, playerxchange,playerychange, key_up, key_down, key_left, key_right, image, it_image,is_it):
        super().__init__(x, y,playerxchange,playerychange, key_up, key_down, key_left, key_right, image,it_image, is_it)

    def arrow_key_handlemovement(self, keys_pressed):
        # if key w is pressed
        if not self.is_it:
            VELOCITY = CONSTANT_VELOCITY
        elif self.is_it:
            VELOCITY = VELOCITY_it #doing 8 instead of VELOCITY because the VELOCITY variable is subject to change and this will reset it every tag

        #if key UP is pressed
        if keys_pressed[self.key_up]:
            # this limits the speed at which the player can travel, if this isn't here then the player will gain 4 velocity
            # for everytime they press "w"
            if self.playerychange == -abs(VELOCITY) or self.playerychange < -abs(VELOCITY):
                self.playerychange = -abs(VELOCITY)
            else:
                self.playerychange -= VELOCITY

        # this key halts movement if the key w isn't pressed down, this works as well for s because it will make both movement varaibles 0
        elif keys_pressed != keys_pressed[self.key_up]:
            self.playerychange = 0

        # if key DOWN is pressed
        if keys_pressed[self.key_down]:
            # this limits the speed at which the player can travel, if this isn't here then the player will gain 4 velocity
            # for everytime they press "w"
            if self.playerychange == VELOCITY or self.playerychange > VELOCITY:
                self.playerychange = VELOCITY
            else:
                self.playerychange += VELOCITY

        # if key LEFT is pressed
        if keys_pressed[self.key_left]:
            # read the comment above for keys "w" and "s" this does the same but for the "a" key.
            if self.playerxchange == -abs(VELOCITY) or self.playerxchange < -abs(VELOCITY):
                self.playerxchange = -abs(VELOCITY)
            else:
                self.playerxchange -= VELOCITY

        # this key halts movement if the key "a" isn't pressed down, this works as well for "d" because it will make both movement varaibles 0
        elif keys_pressed != keys_pressed[self.key_left]:
            self.playerxchange = 0

        # if key RIGHT is pressed
        if keys_pressed[self.key_right]:
            # read the comment above for keys "w", "s" and "a" keys. this does the same but for the "RIGHT/D" key.
            if self.playerxchange == VELOCITY or self.playerxchange > VELOCITY:
                self.playerxchange = VELOCITY
            else:
                self.playerxchange += VELOCITY

    def collide(self):
        if self.is_it:
            self.tag_score += 1
        else:
            pass
        self.tagged()

        self.x, self.y = 936, 300


class Display():
    def __init__(self, size):
        self.size = size
        self.width,self.height = size
        self.screen = pygame.display.set_mode((self.width, self.height))
        if self.size == (800,600):
            self.is_large = False # False mean small
        elif self.size == (1366, 768):
            self.is_large = True #True means large
    def display(self):
        pygame.display.set_mode((self.width, self.height))
    def blit(self,background,location):
       self.screen.blit(background,(location))

    def draw_large(self):
        player1.draw_player_large(self.screen)
        player2.draw_player_large(self.screen)
        pygame.display.update()

    def draw_small(self):
        player1.draw_player_small(self.screen)
        player2.draw_player_small(self.screen)
        pygame.display.update()

    def fill(self,color):
        self.screen.fill(color)


class Scoreboard():
    def __init__(self):
        self.font = pygame.font.SysFont("ebrima",50)
        self.counter = 60
        self.text = str(self.counter)
        self.render_font = self.font.render(str(self.text),True,(255,255,255))
        self.dice_roll_num = random.randint(0, 100)
        self.player1_is_it = False
        self.player2_is_it = True


    def draw_text(self,text):
        Surface_text = self.font.render(text,True,(255,255,255))
        return Surface_text #this needs to return this image to be passed into screen.blit as an surface.


    def dice_roll(self):
        self.dice_roll_num = random.randint(0,100)
        if self.dice_roll_num > 50:
            self.player1_is_it = True
            self.player2_is_it = False
        elif self.dice_roll_num < 50:
            self.player1_is_it = False
            self.player2_is_it = True


    def player1_bool(self):
        if self.player1_is_it:
            return True
        elif not self.player1_is_it:
            return False


    def player2_bool(self):
        if self.player2_is_it:
            return True
        elif not self.player2_is_it:
            return False


# FUNCTIONS
def menu(): #ToDo: implement this as a gui in pygame menu. This is a temp placeholder.
    global screen
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
    global player1, player2, size, scoreboard
    screen = Display(menu())
    screen.display()
    running = True
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT,1000) #ToDo: Set a timer for every loop which will stop gamelay
    player1.set_initial_player_it_image()
    player2.set_initial_player_it_image()
    pygame.display.update()
    while running:
        clock.tick(FPS)
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if you press on the exit in the top right then it will stop the program
                running = False
            if event.type == pygame.USEREVENT:
                scoreboard.counter -= 1
                scoreboard.text = str(scoreboard.counter)
                if player1.is_it:
                    player2.tag_score += 1
                elif player2.is_it:
                    player1.tag_score += 1
                if scoreboard.counter < 0: #if the game timer runs out
                    screen.blit(background, (0, 0))
                    if player1.tag_score > player2.tag_score:
                        screen.blit(scoreboard.draw_text("PLAYER 1 WINS"), (600, 300))
                        pygame.display.update()
                        pygame.time.delay(5000)
                        #screen.blit(scoreboard.font.render((scoreboard.text),True, (255,255,255)), (683, 384))
                    if player2.tag_score > player1.tag_score:
                        screen.blit(scoreboard.draw_text("PLAYER 2 WINS"), (600, 300))
                        pygame.display.update()
                        pygame.time.delay(5000)
                        # screen.blit(scoreboard.font.render((scoreboard.text),True, (255,255,255)), (683, 384))
        screen.blit(scoreboard.draw_text(str(scoreboard.text)),(683,384))
        screen.blit(scoreboard.draw_text("TIME REMAINING:"),(500,280))
        screen.blit(scoreboard.draw_text("player 1 score:" + str(player1.tag_score)),(100,50))
        screen.blit(scoreboard.draw_text("player 2 score:" + str(player2.tag_score)),(500,50))
        keys_pressed = pygame.key.get_pressed()
        player1.wasd_handlemovement(keys_pressed)
        player2.arrow_key_handlemovement(keys_pressed)
        player1.y += player1.playerychange
        player1.x += player1.playerxchange
        player2.x += player2.playerxchange
        player2.y += player2.playerychange
        if screen.is_large: #if the screen is large
            player1.border_large()
            player2.border_large()

            screen.draw_large()
            Player.collide_large_screen(player1,player2)


        elif not screen.is_large: #if the screen is small
            player1.border_small()
            player2.border_small()
            Player.collide_small_screen(player1,player2)

            screen.draw_small()
    pygame.quit()

scoreboard = Scoreboard()
scoreboard.dice_roll()

player1 = wasd_player(936,200,0,0,pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d, player1ship,spaceship_it,scoreboard.player1_bool())
player2 = arrow_key_player(200,300,0,0,pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT, player1ship,spaceship_it,scoreboard.player2_bool())
main()
