import pygame
from loading_images_and_variables import *
import random
class Scoreboard:
    def __init__(self):
        self.font = pygame.font.SysFont("sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic",50)
        self.clock_font = pygame.font.SysFont("franklingothicmedium",100)
        self.counter = 5
        self.text_counter = str(self.counter)
        self.render_font = self.clock_font.render(str(self.text_counter), True, (255, 255, 255))
        self.clock_render_font = self.clock_font.render(str(self.text_counter), True, (0, 0, 0))
        self.dice_roll_num = random.randint(0, 100)
        self.player1_is_it = False
        self.player2_is_it = True


    def draw_text(self,text):
        Surface_text = self.font.render(text,True,(255,255,255))
        return Surface_text #this needs to return this image to be passed into screen.blit as an surface.

    def draw_timer(self,text):
        Surface_text = self.clock_font.render(text,True,(255,255,255))
        return Surface_text



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