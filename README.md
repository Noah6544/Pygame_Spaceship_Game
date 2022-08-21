# Pygame Spaceship Game
Little spaceship game I'm working on in freetime to learn pygame more.

## Reason
- Improve python skills in general, learn OOP more, learn pygame.
- The reason to make the game is to learn pygame more and to have a game to show to my friends to impress them, obviously. 
- I also need something to occupy me in my free period so this is a great little project.

## How to play
- Open in an IDE, and run the "Version 0.6" file. 
- Alternatively, open CMD, cd (change dir) to where "Version 0.6" is (or type cmd in the command bar where the file is), the type "py Version 0.6.py"

## Current Game Objective:
- The player with a yellow outline is it. They may try to tag the other player. Upon collision, the "it" status changes, and the game of tag continues. For every second the "not-it" player manages to evade the "it" player they gain 1 point. At the end of a 60 second countdown, the player with more points wins. 
- There is a slight speed debuff on the "it" player to make the game more balanced, allowing "juking" strategies to be made, this was discovered through play testing with my friends. Without the speed debuff, the "it" player simply has to "W-key" towards the other player and there is absolutely nothing the other player can do as they inevitably get cornered.
- Everytime a new round is initiated (when version 0.6 is run), each player has a 50/50 chance of being "it". This way there is a bit of randomness, and a bit of fairness, in deciding who is "it". Especially because, in the current state of the game, the player roles may not be 100% balanced.


## Future Game Objectives (ideas):
- Create a UI with a minigame selection area to go into different minigames (More valuable learning experience to make a few smaller games with the biggest game elements staying the same through projects)
- Both players have to shoot precise targets that are moving at one end of the screen. First to 3 rounds win
- Make this a minigame-game of sorts, which would be difficult to implement, but rewarding to accomplish.
- For the Tag game, make it a best 2 of 3 rounds to wins, or first to 3 rounds wins.


## Updates:
# Version 0.6 (8/21/22)

Summary: Game is pretty much done! Win Screen Overhaul! I pretty much finished the game. Version 0.6 only has 1 major bug.


### New features:
- Added a replay game option, and fixed the yes/no features at the end of the game to play again
- Added a quality of life feature (surprised it was quick to add) that shows a fun little message every time players collide
- Added and fixed a function which centers text when added (when applicable)

### Bugs fixed and changes:
- Edited UI for score
- When the game is delayed upon collision, the game gains the lost second back, balancing gameplay.
- Win screen bug has been squashed.
 - Continued fine tuning the speed mechanics to continue balancing with play testing.
 - Finding best font to fit the game
- Lowering speed in end screen so a player doesn't accidentally chose one choice or the other.

### ToDo (in order of importance):
- Fix the major end screen trail bug
- Implement a way for players to select how many games they want to play, and if they want to play a series of games (Ex. first to 3, first to 5).
- Add a countdown for when the game starts
- Possibly implement sprite animation?? (this would be fun to try, and would definitely add polish to the game, but this may be saved for down the road).


### Known Issues:
- On the win screen, the winner has a trail behind them as they move. Version 0.6 has taken COUNTLESS hours of debugging a specific issue where the game couldn't restart itself, so all the files were reread and checked over and over for months. Just a few days ago I had a breakthrough and in the last 2 hours many features have been added. Unsolicited rant over.
- The smaller scale game is just broken, everything about it is broken. I need to work on it before it gets so far behind the large scale game that I can't remember how to implement the changes. It is going to get deleted.

I'm very pleased that this project is pretty much over, and that I can wrap up things with Version 1, leaving the game at a state where I've gained a lot of experience learning how to commit push and pull with git, documenting progress, and learning to think in OOP, and as a programmer more.

I'm so happy, I can't explain it. This version has been worked on for almost like 6 or 7 months now, which is embarrassing but balancing school and stuff, this was just an inbetween project, inbetween other projects and school. I finally was able to fix the impossible bugs that made me almost drop this project and just add features that are kinda cool. Pretty basic game that others could make in a few days, but this is mine. all mine.

### VERSION 1 VERY SOON!
