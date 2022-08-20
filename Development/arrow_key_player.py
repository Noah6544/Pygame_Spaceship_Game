import pygame
import random
from settings import *
from player import Player
class arrow_key_player(Player):
    def __init__(self, x, y, playerxchange,playerychange, key_up, key_down, key_left, key_right, image, it_image,is_it):
        super().__init__(x, y,playerxchange,playerychange, key_up, key_down, key_left, key_right, image,it_image, is_it)

    def arrow_key_handlemovement(self, keys_pressed):
        # if key w is pressed
        if not self.is_it:
            self.Velocity = self.Constant_Velocity
        elif self.is_it:
            self.Velocity = self.Velocity_it #doing 8 instead of VELOCITY because the VELOCITY variable is subject to change and this will reset it every tag

        if self.won == True:
            self.Velocity = self.Velocity_End_Screen

        #if key UP is pressed
        if keys_pressed[self.key_up]:
            # this limits the speed at which the player can travel, if this isn't here then the player will gain 4 velocity
            # for everytime they press "w"
            if self.playerychange == -abs(self.Velocity) or self.playerychange < -abs(self.Velocity):
                self.playerychange = -abs(self.Velocity)
            else:
                self.playerychange -= self.Velocity

        # this key halts movement if the key w isn't pressed down, this works as well for s because it will make both movement varaibles 0
        elif keys_pressed != keys_pressed[self.key_up]:
            self.playerychange = 0

        # if key DOWN is pressed
        if keys_pressed[self.key_down]:
            # this limits the speed at which the player can travel, if this isn't here then the player will gain 4 velocity
            # for everytime they press "w"
            if self.playerychange == self.Velocity or self.playerychange > self.Velocity:
                self.playerychange = self.Velocity
            else:
                self.playerychange += self.Velocity

        # if key LEFT is pressed
        if keys_pressed[self.key_left]:
            # read the comment above for keys "w" and "s" this does the same but for the "a" key.
            if self.playerxchange == -abs(self.Velocity) or self.playerxchange < -abs(self.Velocity):
                self.playerxchange = -abs(self.Velocity)
            else:
                self.playerxchange -= self.Velocity

        # this key halts movement if the key "a" isn't pressed down, this works as well for "d" because it will make both movement varaibles 0
        elif keys_pressed != keys_pressed[self.key_left]:
            self.playerxchange = 0

        # if key RIGHT is pressed
        if keys_pressed[self.key_right]:
            # read the comment above for keys "w", "s" and "a" keys. this does the same but for the "RIGHT/D" key.
            if self.playerxchange == self.Velocity or self.playerxchange > self.Velocity:
                self.playerxchange =  self.Velocity
            else:
                self.playerxchange +=  self.Velocity



    def collide(self):
        if self.is_it:
            self.tag_score += 1
        else:
            pass
        self.tagged()

        self.x, self.y = 936, 300
