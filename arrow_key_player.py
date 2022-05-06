import pygame
import random
from loading_images_and_variables import *
from player import Player
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
