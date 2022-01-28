# Remote-Control-Game
Playing a Python game using a real remote control with Arduino.

The goal of the game is to avoid falling obstacles by moving left or right. In the original game, player was moved using left and right arrow keys.
First version of the game was designed and programmed by cagey-squirrel. 
The original version was modified so that the movement of the player is initiated by button presses on a real remote control. Buttons that will be used for the game are predetermined and the identification of their IR codes is done prior to this project.
Arduino is used for the acquisition of IR signals, and its result is sent via serial interface to Python game which then decodes them and move the player at the right directions.

You can see the final project on YT: https://www.youtube.com/watch?v=V8U2r5bWeUY&t=7s
