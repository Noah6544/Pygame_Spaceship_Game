import pygame
import random


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
black = ((0,0,0))
white = (255,255,255)
random_collide_phrases = ["Gotcha!", "Finally!!!", "You're it!", "Tag!", "Ha, you suck!", "Almost got away!",
                               "I'm just better.", "You could never get away.", "BAng!", "Terron is money",
                               "AYEE", "Nice one!!" "What'd you say??", "Got you!", "too easy honestly.",
                               "oops", "hey lets go!", "LETS GOOOO!!!", "I'm not even trying bro","it doesn't count I'm not trying",]

collide_font = pygame.font.SysFont("C:\\Users\\Noah\'s Marc P. 4648\\AppData\\Local\\Microsoft\\Windows\\Fonts\\it font.tff",100) #putting this in settings because I'm getting an error with it being in scoreboard for some reason

def random_collide_phrase():
    return random.choice(random_collide_phrases)

# variables
global play_again
global temp_play_again
temp_play_again = None
play_again = True
win_loop = True
FPS = 60

