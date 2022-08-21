import pygame
from settings import *
import random
class Scoreboard:
    def __init__(self):
        self.font = pygame.font.SysFont("centurygothic",45)
        self.clock_font = pygame.font.SysFont("centurygothic",50)
        self.counter = 60
        self.text_counter = str(self.counter)
        self.dice_roll_num = random.randint(0, 100)
        self.player1_is_it = False
        self.player2_is_it = True

    def draw_text(self,text,color,font):
        Surface_text = font.render(text,True,color)
        return Surface_text #this needs to return this image to be passed into screen.blit as an surface.

    def draw_text_location(self,text,color,font,screen,width_offset,height_offset): #this functions purpose is to return the rectangle to be used in centering text.
                                                         # its identical to the function above. but with screen agrument/input and a rectangle variable
        Surface_text = self.font.render(text,True,color)
        Surface_text_rect = Surface_text.get_rect(center=(screen.width/2 + width_offset,screen.height/2 + height_offset))
        return Surface_text_rect #this needs to return this image to be passed into screen.blit as an surface.


    def dice_roll(self):
        self.dice_roll_num = random.randint(0,100)
        if self.dice_roll_num >= 50:
            self.player1_is_it = True
            self.player2_is_it = False
        elif self.dice_roll_num <= 49:
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
