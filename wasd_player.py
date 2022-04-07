import pygame
import random
from loading_images_and_variables import *
from player import Player
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
        pygame.time.delay(1000) # only one function needs this, not both, because it will delay the entire game.