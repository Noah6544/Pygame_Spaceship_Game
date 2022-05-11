# Pygame Spaceship Game
Little spaceship game I'm working on in freetime to learn pygame more.

## Reason
- Improve python skills in general, learn OOP more, learn pygame.
- The reason to make the game is to learn pygame more and to have a game to show to my friends to impress them, obviously. 
- I also need something to occupy me in my free period so this is a great little project.

## How to play
- Open in an IDE, and run the "Version 0.5" file. 
- Alternatively, open CMD, cd (change dir) to where "Version 0.5" is (or type cmd in the command bar where the file is), the type "py Version 0.5.py"

## Current Game Objective:
- The player with a yellow outline is it. They may try to tag the other player. Upon collision, the "it" status changes, and the game of tag continues. For every second the "not-it" player manages to evade the "it" player they gain 1 point. At the end of a 60 second countdown, the player with more points wins. 
- There is a slight speed debuff on the "it" player to make the game more balanced, allowing "juking" strategies to be made, this was discovered through play testing with my friends. Without the speed debuff, the "it" player simply has to "W-key" towards the other player and there is absolutely nothing the other player can do as they inevitably get cornered.
- Everytime a new round is initiated (when version 0.5 is run), each player has a 50/50 chance of being "it". This way there is a bit of randomness, and a bit of fairness, in deciding who is "it". Especially because, in the current state of the game, the player roles may not be 100% balanced.


## Future Game Objectives (ideas):
- Create a UI with a minigame selection area to go into different minigames (More valuable learning experience to make a few smaller games with the biggest game elements staying the same through projects)
- Both players have to shoot precise targets that are moving at one end of the screen. First to 3 rounds win
- Make this a minigame-game of sorts, which would be difficult to implement, but rewarding to accomplish.
- For the Tag game, make it a best 2 of 3 rounds to wins, or first to 3 rounds wins.


## Updates:
# Version 0.5 

Summary: UI has been Overhauled!!

### Completed:
 - UI has been overhauled, 
 - Split the game into multiple files, making game mangment much simpler.
 - Continued fine tuning the speed mechanics to continue balancing with play testing.

### ToDo:
- Fix the win screen (the winning player is to be the only one on screen, then they can either choose to play again or quit the game, by moving to one of the 2 boxes)
- Add a countdown for when the game starts
- Implement a way for players to select how many games they want to play, and if they want to play a series of games (Ex. first to 3, first to 5).
- Fix the smaller scale game, the timer is scaled wrong, and the place holder "it" images aren't working.
- Possibly implement sprite animation?? (this would be fun to try, and would definitly add polish to the game, but this may be saved for down the road).

### Known Issues:
- The smaller scale game is just broken, everything about it is broken. I need to work on it before it gets so far behind the large scale game that I can't remember how to implement the changes
- The win screen is......insufferable

I'm quite pleased how this development is going, especially as I haven't worked on the game as seriously in the past few months, but as summer draws nearer and I'm finishing up my exams, I seem to have some more time on my hands. This game is seeming to be almost like an actual game.

### VERSION 0.6 SOON!
