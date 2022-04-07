import pygame
from loading_images_and_variables import *
import random
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
        self.not_it_image_small = not_it_image

        self.image_small = pygame.transform.scale(self.not_it_image_small,(100,100))
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