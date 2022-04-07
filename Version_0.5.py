
import pygame
import random
from loading_images_and_variables import *
from player import Player
from wasd_player import wasd_player
from arrow_key_player import arrow_key_player
from Scoreboard import Scoreboard
# Initialize
pygame.init()


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

    def main_loop_actions(self): # a function just to clean up the main loop things that happen each loop
        self.blit(scoreboard.draw_timer(str(scoreboard.text_counter)), (683, 384))
        self.blit(scoreboard.draw_text("Score: " + str(player1.tag_score)), (player1.x - 20, player1.y - 80))
        self.blit(scoreboard.draw_text("Score: " + str(player2.tag_score)), (player2.x - 20, player2.y - 80))
        keys_pressed = pygame.key.get_pressed()
        player1.wasd_handlemovement(keys_pressed)
        player2.arrow_key_handlemovement(keys_pressed)
        player1.y += player1.playerychange
        player1.x += player1.playerxchange
        player2.x += player2.playerxchange
        player2.y += player2.playerychange
        if self.is_large: #if the screen is large
            player1.border_large()
            player2.border_large()
            self.draw_large()
            Player.collide_large_screen(player1,player2)
        elif not self.is_large: #if the screen is small
            player1.border_small()
            player2.border_small()
            Player.collide_small_screen(player1,player2)
            self.draw_small()

#    def main_loop_executions(self):


# FUNCTIONS

class Scene():
    def __init__(self):
        pass

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

    def win_screen(screen):
        global player1, player2, size, scoreboard
        if player1.tag_score > player2.tag_score:
            player2.x = 100000
            player2.y = 10000000
            player1.x = 683
            player1.y = 683
            screen.blit(scoreboard.draw_text("PLAYER 1 WINS"), (screen.width / 2, screen.height / 2))
            screen.draw_large()
        if player2.tag_score > player1.tag_score:
            player1.x = 10000000
            player1.y = 1000000
            player2.x = 683
            player2.y = 384
            screen.blit(scoreboard.draw_text("PLAYER 2 WINS"), (600, 300))
            screen.draw_large()

    def main(self):
        play_again = True
        global player1, player2, size, scoreboard
        screen = Display(self.menu())
        screen.display()
        running = True
        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT,1000) #this is a timer that will tick once per second and is the main time engine
        player1.set_initial_player_it_image()
        player2.set_initial_player_it_image()
        pygame.display.update()
        while running:
            clock.tick(FPS)
            screen.fill(black_background)
            for event in pygame.event.get():
                #while play_again:
                if event.type == pygame.QUIT: # if you press on the exit in the top right then it will stop the program
                    running = False
                if event.type == pygame.USEREVENT:
                    scoreboard.counter -= 1
                    scoreboard.text_counter = str(scoreboard.counter)
                    if player1.is_it:
                        player2.tag_score += 1
                    elif player2.is_it:
                        player1.tag_score += 1
                    if scoreboard.counter < 0: #if the game timer runs out
                        win_screen(screen)
                        break


            screen.main_loop_actions()


        pygame.quit()

scoreboard = Scoreboard()
scoreboard.dice_roll()

player1 = wasd_player(936,200,0,0,pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d, player1ship,spaceship_it,scoreboard.player1_bool())
player2 = arrow_key_player(200,300,0,0,pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT, player1ship,spaceship_it,scoreboard.player2_bool())
Scene.main()

#region

#regoin
