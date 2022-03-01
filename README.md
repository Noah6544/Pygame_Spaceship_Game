# Pygame_Spaceship_Game
Little spaceship game I'm working on in freetime to learn pygame more.
## Reason
- Improve python skills in general, learn OOP more, learn pygame.
- The reason to make the game is to learn pygame more and to have a game to show to my friends to impress them, obviously. 
- I also need something to occupy me in my free period so this is a great little project.
## Game Objective:
- Create a UI with a minigame selection area to go into different minigames (More valuable learning experience to make a few smaller games with the biggest game elements staying the same through projects)
- I think a tag game would be interesting, the movement for some reason feels pretty smooth, or maybe I'm just appreciating it being bug free.
- Another idea is that both players have to shoot precise targets that are moving at one end of the screen. First to 3 rounds win
- Another Another idea is to make this a minigame of sorts, which would be difficult to implement, but rewarding to accomplish.
## Updates:
### Version 0.3

Accomplished A LOT in this version so far

### Completed:
  - Created a new hitbox for scaled down ships, as my friends said that the ships should be smaller on the smaller screen size(800x600). 
 - Nerfed (with surprising ease due to all the interconnecting variables in my usual code which normally would've made it impossible to change it) the player that is it. They are slightly slower than the person who is being chased, as I realized that the person who is "it" is too overpowered, and can just chase down the person not "it" with no penalty, which makes the game less fun, and juking the "it" player more difficult (but when juked it was satisfying).
 - Began implementing a menu system (although it is text now, it serves as a placeholder for options such as screen size and, in the future, player ship image/color)
- Created a new screen class for drawing and displaying screen functions (not sure if this is good code, as I don't think it makes anything more clean or less redundant, but I think it was a good idea to continue to learn class implementation and work on OOP. I think I fixed what wasn't broken but I'm moving towards just OOP for this code)
- Just about entirely converted to all OOP and classes, only have 2 outstanding function which are pretty necessary to the program. Everything is extremely scalable
### Work in progress:
 - Implementing menu into a new pygame screen,  currently it is just a string system, however, I think it can be done with decent ease once I begin.
 - Create a new image to polish the player who is "it" because a yellow square isn't that great.
### ToDo:
 - Create menu GUI
 - Create a looping game mode: a timer counting down and point awarded for tags. Most tags win

I think this game is slighty fun with friends as everyone I've played with enjoys it for at least a minute before it gets repetitive because there's no goal, but I'm just working on bare bones now, polish beginning soon.
