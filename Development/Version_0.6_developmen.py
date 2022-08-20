
import pygame
import random
import settings
from settings import *
from settings import black_background


from player import Player
from wasd_player import wasd_player
from arrow_key_player import arrow_key_player
from Scoreboard import Scoreboard


class Display:
    def __init__(self, size):
        self.size = size
        self.width,self.height = size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.play_again_hitbox_left = pygame.Rect(5, 250, 300, 300)
        self.play_again_hitbox_right = pygame.Rect(1065, 250, 300, 300)  #values: moving leftright, up/down, width, heigh
        if self.size == (800,600):
            self.is_large = False # False mean small
        elif self.size == (1366, 768):
            self.is_large = True #True means large
    def display(self):
        pygame.display.set_mode((self.width, self.height))
    def blit(self,background,location):
       self.screen.blit(background,(location))
    def draw_large(self): #updates
        if scoreboard.counter >= 0:
            player1.draw_player_large(self.screen)
            player2.draw_player_large(self.screen)
            pygame.display.update()
        elif scoreboard.counter < 0:

            if player1.won:
                self.blit(scoreboard.draw_text("Player 1 Wins",(255,255,255)), (470, 20))
                player1.draw_player_large(self.screen)
            if player2.won:
                self.blit(scoreboard.draw_text("Player 2 Wins",(255,255,255)), (470, 20))

                player2.draw_player_large(self.screen)
            pygame.draw.rect(self.screen, (255, 0, 0), self.play_again_hitbox_right,2)
            pygame.draw.rect(self.screen, (10, 10, 255), self.play_again_hitbox_left,3)
            self.blit(scoreboard.draw_text("Play Again?",(255,255,255)),(476,600))
            self.blit(scoreboard.draw_text("Yes",(0,0,255)),(110,360))
            self.blit(scoreboard.draw_text("No",(255,0,0)),(1180,360)) #ToDo Polish these positions to be pixel perfect and cleaner.
            pygame.display.update()


    def draw_small(self):
        player1.draw_player_small(self.screen)
        player2.draw_player_small(self.screen)
        pygame.display.update()

    def fill(self,color):
        self.screen.fill(color)

    def main_loop_actions(self): # a function just to clean up the main loop things that happen each loop
        if scoreboard.counter >= 0:
            self.blit(scoreboard.draw_timer(str(scoreboard.text_counter)), (683, 384))
            self.blit(scoreboard.draw_text("Score: " + str(player1.tag_score),(255,255,255)), (player1.x - 20, player1.y - 80))
            self.blit(scoreboard.draw_text("Score: " + str(player2.tag_score),(255,255,255)), (player2.x - 20, player2.y - 80))
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
            Player.collide_large_screen(player1,player2,self.play_again_hitbox_left,self.play_again_hitbox_right)
            self.draw_large()

        elif not self.is_large: #if the screen is small
            player1.border_small()
            player2.border_small()
            Player.collide_small_screen(player1,player2)
            self.draw_small()

    def win_loop_actions(self):# a function just to clean up the main loop things that happen each loop
        if player1.won:
            keys_pressed = pygame.key.get_pressed()
            player1.wasd_handlemovement(keys_pressed)
            player1.y += player1.playerychange
            player1.x += player1.playerxchange
        elif player2.won:
            keys_pressed = pygame.key.get_pressed()
            player2.arrow_key_handlemovement(keys_pressed)
            player2.x += player2.playerxchange
            player2.y += player2.playerychange
        if self.is_large: #if the screen is large
            if player1.won:
                player1.border_large()
            elif player2.won:
                player2.border_large()
            if Player.collide_large_screen(player1,player2,self.play_again_hitbox_left,self.play_again_hitbox_right): #if they select yes
                self.draw_large()
                return True
            elif Player.collide_large_screen(player1,player2,self.play_again_hitbox_left,self.play_again_hitbox_right): #if they select no
                self.draw_large()
                return False

            elif Player.collide_large_screen(player1,player2,self.play_again_hitbox_left,self.play_again_hitbox_right) == None:
                pass

            else:
                self.draw_large()
                return None

            self.draw_large()


        elif not self.is_large: #if the screen is small, broken don't select small option.
            if player1.won:
                player1.border_small()
            elif player2.won:
                player2.border_small()
            self.draw_small()

# FUNCTIONS

def start(self):
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000)  # this is a timer that will tick once per second and is the main time engine
    player1.set_initial_player_it_image()
    player2.set_initial_player_it_image()
    pygame.display.update()

def menu(): #ToDo: implement this as a gui in pygame menu. This is a temp placeholder.
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
count = 0
def win_screen(screen):
    global player1, player2, size, scoreboard, play_again, count
    running = True
    clock = pygame.time.Clock()
    player2.set_winner_image()
    player1.set_winner_image()

    screen.fill(black_background)

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            # while play_again:
            if event.type == pygame.QUIT:  # if you press on the exit in the top right then it will stop the program
                running = False

        Display_win_loop_actions_bool = Display.win_loop_actions(screen)

        if Display_win_loop_actions_bool: #if they select yes
            running = False
            return True
        elif Display_win_loop_actions_bool == False:# if they select no #make sure you do ==, becase "elif not bool" means none too
            running = False
            pygame.quit()
        elif Display_win_loop_actions_bool != True or Display_win_loop_actions_bool != False: #if they haven't selected
            running = True

        if not settings.play_again:
            return False
        if settings.play_again and Display_win_loop_actions_bool == True: #YESS FINALLY DEBUGGING IS GREAT I OVERLOOKED THAT PLAY AGAIN IS DEFAPULTE TO YES.
            return True

def main():
    global player1, player2, scoreboard, play_again
    screen = Display(menu())
    screen.display()
    running = True
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT,1000)  # this is a timer that will tick once per second and is the main time engine
    player1.set_initial_player_it_image()
    player2.set_initial_player_it_image()
    pygame.display.update()
    while running:
        clock.tick(FPS)
        screen.fill(black_background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you press on the exit in the top right then it will stop the program
                pygame.quit()
            if event.type == pygame.USEREVENT:
                scoreboard.counter -= 1
                scoreboard.text_counter = str(scoreboard.counter)
                if player1.is_it:
                    player2.tag_score += 1
                elif player2.is_it:
                    player1.tag_score += 1
                if scoreboard.counter < 0:  # if the game timer runs out
                    if player1.tag_score > player2.tag_score:  # if player 1 wins
                        player1.won = True
                        player2.won = False
                        player2.move(10000, 1000)
                        player1.move(300,350)
                    if player2.tag_score > player1.tag_score:  # if player 2 wins
                        player2.won = True
                        player1.won = False
                        player1.move(10000, 10000)
                        player2.move(300,350)
                    elif player2.tag_score == player1.tag_score:  # this is if I'm debugging just the win loop
                        player1.won = True
                        player2.won = False
                        player1.move(365, 768)
                        player2.move(10000, 1000)

                    win_screen_bool = win_screen(screen)
                    if win_screen_bool == True:
                        return True
                    elif win_screen_bool == False:

                       # pygame.quit()
                       return False
                    else:
                        pass
                   # running = False

        Display.main_loop_actions(screen)

    if not settings.play_again:
        return False

    elif settings.play_again:
        return True

while settings.play_again: #while the player wants to keep playing
    # Initialize
    pygame.init()

    num_of_games = 0
    scoreboard = Scoreboard()
    scoreboard.dice_roll()

    player1 = wasd_player(936,200,0,0,pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d, player1ship,spaceship_it,scoreboard.player1_bool())
    player2 = arrow_key_player(200,300,0,0,pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT, player1ship,spaceship_it,scoreboard.player2_bool())

    if main(): #if main returns true, and therefore the game should repeat:
        pass
    if not main(): #if main returns false, and therefore game is over:
        pygame.quit()
        print("clean break")
        break

    if num_of_games <= 1:
        print("You've played 1 game!")
    elif num_of_games > 1:
        print(f"You've played {num_of_games} games!")
    num_of_games += 1
    pygame.quit()
#while true:
    #start the game
    #if the player chooses to play again, restart the game
    #if the player chooses to stop the game, quit the game.
