# Versions:
## Class integration (2/18/22) (Version 0.0)
 - Began creating classes for player1, fleshed out the first class. 
# Version 0.1 (2/23/22)
 - Been putting off updating this for some time because I was having trouble with the pygame.rect object and the pygame.Rect.colliderect functions. I thought that it was above what I was able to do but it was extremely easy and pretty fast. Lesson learned: Always try  before giving up, and before you give up, make sure you know why. Don't just "ah I can't do this" instead, make sure its something more like, "I can't get this done because I don't know how to work with parent and child inheritance classes and I don't have time right now. Don't give up when you're frustrated, chances are, you're about to hit gold.
 -Integrated the new inheritance class was a ton easier than i thought it was going to be. super function is a life-saver, just the other day i was looking at it thinking I wasn't going to use it until im wayy more experiences, but wow. 
 - Integrated new collisions with rectangle objects and have them reset positions on collisions, will continue to buildup the bare bones of the program then polish this minigame. I will then make a UI menu to select minigames
# Version 0.2 (2/25/22)
### Completed: 
 - Wrapped up integration of old outstanding functions into classes for the arrow key and wasd players. 
 - Completely deleted the old "enemy" variable from when I didn't fully have a complete vision.
Also doing some laptop coding on the drive back for about 2 or so hours.
 - Randomly selects who is 'it" at the start of the game
 - a TEMPORARY visual replacement for who is it with a yellow border (all I could manage with ms paint due to not having any photo editing software currently avaliable on this laptop, will make a more final image on main pc

 ### ToDo:
  - Edit the image for player who's "it"  instead of having a yellow box.
  - Create a text that will attatch to the player who's it and will say "IT!" or something similar
  - Create a scoreboard for everytime a player is tagged, and possibly a timer counting down to see who can get the most tags
  - An ending UI prompting players to play again/go to another minigame.
 
# Version 0.3 (3/1/22)

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

# Version 0.4 😪

Summary: 😔 Mainly just debugging for a month, but I implemented A LOT of important things in this version
### Completed:
- Made a visual timer system in which the player who is not it gains a point every second they manage to not be tagged, and at the end of a minute the player with the more points wins
- A random dice roll feature which randomly picks the player who is it.
- I don't remember everything I added, even though it wasn't a lot for a months work, because I was debugging for the majority of the time

### ToDo:
 - Make the timer system more visually pleasing, scale the timer system for the smaller scale game
- Fix the smaller scale game, the timer is scaled wrong, and the place holder "it" images aren't working.

### Known Issues:
 - The smaller scale game is just broken, everything about it is broken. I need to work on it before it gets so far behind the large scale game that I can't remember how to implement the changes

### Debug rant:
I had a bug which the players weren't decreasing speed, and the placeholder image for who's it was remaing and both players were it. There was also issues where they had the same speed. This took over a month to resolve, and I debugged so much (going into, retrospectively, unnecessary things, such as the movement, trying to fix it. I broke the movement at one point because I thought that was the fix.
The actual fixes were quite simple of course, just had to keep consistently coming back and chip away at it. 

Lots of fun but this update drained me, took so many hours of unsuccessful debugging but I learned a lot about perseverance and PyCharm debugger. 
I also re-read this whole file about 20 times so at least I understand more.


